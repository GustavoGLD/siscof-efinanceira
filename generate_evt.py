import re
import textwrap
from xmlschema import XMLSchema, XsdElement
from xmlschema.validators import XsdSimpleType, XsdAtomicBuiltin, XsdComplexType
from pathlib import Path
from typing import Dict, Optional, Set
import unicodedata

# Templates para geração de código (unchanged)
TEMPLATE_SIMPLE = """
class {classname}:
    \"\"\"{doc}\"\"\"
    def __init__(self, value: {typ}):
{validation}
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "{classname}":
        return cls({cast}val)

    def __str__(self):
        return str(self.value)
"""

TEMPLATE_COMPLEX = """
class {classname}:
    \"\"\"{doc}\"\"\"
    def __init__(self, {ctor_args}):
{assigns}
"""

TEMPLATE_BUILDER = """
class {classname}XmlBuilder(XmlBuilderInterface):
    def build(self, obj: {classname}) -> ET.Element:
        el = XmlAdapter.create_element("{tag}"{attrib})
{children}
        return el
"""

TEMPLATE_TEST_SIMPLE = """
    def test_{tag}(self):
        # Criar um objeto {classname} de exemplo
        obj = {classname}({example_args})
        # No builder for simpleType; manual XML creation for testing
        el = ET.Element('{tag}')
        el.text = str(obj)
        xml_str = ET.tostring(el, encoding='utf-8')
        schema_doc = LET.parse('{schema_path}')
        schema = LET.XMLSchema(schema_doc)
        doc = LET.fromstring(xml_str)
        ok = schema.validate(doc)
        if not ok: print(schema.error_log)
        self.assertTrue(ok)
"""

TEMPLATE_TEST_COMPLEX = """
    def test_{tag}(self):
        # Criar um objeto {classname} de exemplo
        obj = {classname}({example_args})
        builder = {classname}XmlBuilder()
        self.validar_xml(obj, builder, "{schema_path}")
"""

# Mapeamento de tipos XML para Python (unchanged)
TYPE_MAPPING = {
    str: "str",
    int: "int",
    float: "float",
    bool: "bool",
    "xs:string": "str",
    "xs:unsignedInt": "int",
    "xs:ID": "str",
    "xs:date": "str",  # Tratar xs:date como string for from_str
}


# Função para converter snake_case para CamelCase (unchanged)
def snake_to_camel(s):
    return ''.join(p.capitalize() for p in s.split('_'))


# Função para extrair namespace e nome do elemento (unchanged)
def split_ns_name(elem_name: str, ns_map: Dict[str, str]) -> tuple[str, str]:
    if "}" in elem_name:
        ns, name = elem_name.split("}")
        ns = ns[1:]  # Remove '{'
        prefix = next((k for k, v in ns_map.items() if v == ns), "")
        return prefix, name
    return "", elem_name


# Função para sanitizar strings (unchanged)
def sanitize_string(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'\s+', ' ', text.strip())
    return text


# Função auxiliar para gerar argumentos de teste para um elemento
def generate_test_args(elem: XsdElement, ns_map: Dict[str, str], target_ns: str) -> str:
    if isinstance(elem.type, XsdSimpleType):
        # Para simpleType, gerar valor de exemplo com base no tipo e facets
        tipo: XsdAtomicBuiltin = elem.type.primitive_type
        python_type = tipo.python_type
        typ = TYPE_MAPPING.get(python_type, "str")
        # Valor padrão baseado no tipo
        example_value = "1" if typ == "int" else "example"

        # Ajustar com base no nome do elemento
        if "cnpj" in elem.local_name.lower():
            example_value = "12345678000195"  # Formato CNPJ válido
        elif "date" in tipo.name:
            example_value = "2023-01-01"  # Formato de data ISO
        elif "base64Binary" in tipo.name:
            example_value = "SGVsbG8="  # Exemplo de string base64 ("Hello")

        # Ajustar com base em facets (patterns)
        if elem.type.facets.get("pattern"):
            pattern = elem.type.facets["pattern"].pattern
            # Mapear padrões para valores de exemplo
            pattern_map = {
                "[1|2|3]": "1",
                "[1|2]": "1",
                "[1;3;5]": "1",
                "[1]": "1",
                "[0-9]{1,18}[-][0-9]{2}[-][0-9]{3}[-][0-9]{4}[-][0-9]{1,18}": "123-12-123-1234-123",
                "[0-9]{14}": "12345678000199",
                "[0-9]{1,21}": "123456789012345678901",
                "[0-9]{1,2}": "12",
                "20([0-9][0-9])(0[1-9]|1[0-3])": "202301",
                "[0-9]{1,19}[,][0-9]{2}": "12345678901234567,89",
                "[-]{0,1}[0-9]{1,19}[,][0-9]{2}": "-12345678901234567,89",
            }
            example_value = pattern_map.get(pattern, example_value)

        # Ajustar com base em enumerações
        elif elem.type.facets.get("enumeration"):
            enum_values = [e.value for e in elem.type.facets["enumeration"].enumeration]
            example_value = enum_values[0] if enum_values else example_value

        # Ajustar com base em minLength/maxLength
        elif elem.type.facets.get("minLength") or elem.type.facets.get("maxLength"):
            min_length = elem.type.facets.get("minLength", 0).value if elem.type.facets.get("minLength") else 0
            max_length = elem.type.facets.get("maxLength", 100).value if elem.type.facets.get("maxLength") else 100
            example_value = "example"[:max_length]
            if len(example_value) < min_length:
                example_value = example_value + "x" * (min_length - len(example_value))

        # Ajustar com base no tipo (decimal, string, etc.)
        if tipo.local_name == "decimal" and example_value == "example":
            example_value = "1"  # Default para decimal sem padrão específico
        elif tipo.local_name == "string" and example_value == "example":
            # Usar nome do elemento para valores mais significativos
            name_lower = elem.local_name.lower()
            if "nome" in name_lower:
                example_value = "Teste Nome"
            elif "pais" in name_lower:
                example_value = "BR"
            elif "endereco" in name_lower or "logradouro" in name_lower:
                example_value = "Rua Exemplo"
            elif "municipio" in name_lower:
                example_value = "Sao Paulo"
            elif "bairro" in name_lower:
                example_value = "Centro"
            elif "cep" in name_lower:
                example_value = "12345-678"
            elif "uf" in name_lower:
                example_value = "SP"
            elif "numero" in name_lower:
                example_value = "123"
            elif "complemento" in name_lower:
                example_value = "Apto 456"
            elif "andar" in name_lower:
                example_value = "5"
            elif "caixa" in name_lower:
                example_value = "12345"
            elif "tpnif" in name_lower:
                example_value = "1"  # Default para tpNIF, assumindo enumerado [1|2|3]

        return f"{snake_to_camel(elem.local_name)}.from_str({example_value!r})"

    elif isinstance(elem.type, XsdComplexType):
        # Para complexType, construir instância com argumentos recursivos
        args = []
        # Atributos
        for attr_name, attr in elem.type.attributes.items():
            if attr.use == "required":
                attr_typ = TYPE_MAPPING.get(attr.type.name, "str")
                args.append(f"{attr_name}='example_id'" if attr_typ == "str" else f"{attr_name}=1")

        # Elementos filhos
        if hasattr(elem.type.content, "iter_elements"):
            for child in elem.type.content.iter_elements():
                child_name = child.local_name
                if not child_name:
                    continue
                child_camel = snake_to_camel(child_name)
                is_list = child.max_occurs is None or child.max_occurs > 1
                opt = child.min_occurs == 0
                child_arg = generate_test_args(child, ns_map, target_ns)

                # Include all fields (required and optional) with generated args
                if is_list:
                    args.append(f"{child_name}=[{child_arg}]")
                else:
                    args.append(f"{child_name}={child_arg}")

        # Special handling for Nomeoutros to ensure both NomePF and NomePJ are included
        if elem.local_name == "Nomeoutros":
            children = list(elem.type.content.iter_elements())
            nome_pf_arg = generate_test_args(children[0], ns_map, target_ns) if children else "None"
            nome_pj_arg = generate_test_args(children[1], ns_map, target_ns) if len(children) > 1 else "None"
            args = [arg for arg in args if not arg.startswith("NomePF=") and not arg.startswith("NomePJ=")]
            args.append(f"NomePF={nome_pf_arg}")
            args.append(f"NomePJ={nome_pj_arg}")

        # Special handling for Nif to ensure tpNIF, NumeroNIF, and PaisEmissaoNIF are included
        if elem.local_name == "Nif":
            children = list(elem.type.content.iter_elements())
            tp_nif_arg = generate_test_args(children[0], ns_map, target_ns) if children else "TpNif.from_str('1')"
            numero_nif_arg = generate_test_args(children[1], ns_map, target_ns) if len(
                children) > 1 else "Numeronif.from_str('123')"
            pais_emissao_nif_arg = generate_test_args(children[2], ns_map, target_ns) if len(
                children) > 2 else "Paisemissaonif.from_str('BR')"
            args = [arg for arg in args if
                    not arg.startswith("tpNIF=") and not arg.startswith("NumeroNIF=") and not arg.startswith(
                        "PaisEmissaoNIF=")]
            args.append(f"tpNIF={tp_nif_arg}")
            args.append(f"NumeroNIF={numero_nif_arg}")
            args.append(f"PaisEmissaoNIF={pais_emissao_nif_arg}")

        # Se não há argumentos, retornar construtor vazio
        if not args:
            return f"{snake_to_camel(elem.local_name)}()"
        return f"{snake_to_camel(elem.local_name)}({', '.join(args)})"

    return "None"  # Fallback para elementos sem tipo definido (e.g., referências)


# Restante do código (unchanged)
def process_element(
        elem: XsdElement,
        ns_map: Dict[str, str],
        out: Dict[str, list],
        subschema_path: str,
        processed: Set[str],
        target_ns: str
):
    name = elem.local_name
    if name in processed:
        return
    processed.add(name)

    ct = elem.type
    doc = ""
    if elem.annotation and elem.annotation.documentation:
        if isinstance(elem.annotation.documentation, list):
            doc_texts = [d.text for d in elem.annotation.documentation if d.text]
            doc = sanitize_string(" ".join(doc_texts))
        else:
            doc = sanitize_string(elem.annotation.documentation.text or "")
    classname = snake_to_camel(name)
    ns_prefix, tag = split_ns_name(elem.name, ns_map)
    ns = ns_map.get(ns_prefix, target_ns)

    if isinstance(ct, XsdSimpleType):
        tipo: XsdAtomicBuiltin = ct.primitive_type
        python_type = tipo.python_type
        typ = TYPE_MAPPING.get(python_type, "str")
        cast = "" if typ == "str" else f"{typ}("
        checks = []
        for facet_name, facet in ct.facets.items():
            if facet_name == "minLength":
                checks.append(f"        if len(str(value)) < {facet.value}: raise ValueError('{name} inválido')")
            elif facet_name == "maxLength":
                checks.append(f"        if len(str(value)) > {facet.value}: raise ValueError('{name} inválido')")
            elif facet_name == "pattern":
                pattern = sanitize_string(facet.pattern)
                checks.append(f"        if not re.match(r'{pattern}', str(value)): raise ValueError('{name} inválido')")
        validation = "\n".join(checks) or "        pass"
        out["simple"].append(
            TEMPLATE_SIMPLE.format(
                classname=classname,
                doc=doc,
                validation=validation,
                typ=typ,
                cast=cast
            )
        )
    elif isinstance(ct, XsdComplexType):
        fields, assigns, children, example_args, attribs = [], [], [], [], []
        for attr_name, attr in ct.attributes.items():
            if attr.use == "required":
                attr_typ = TYPE_MAPPING.get(attr.type.name, "str")
                fields.append(f"{attr_name}: {attr_typ}")
                assigns.append(f"        self.{attr_name} = {attr_name}")
                attribs.append(f"        el.set('{attr_name}', str(obj.{attr_name}))")
                example_args.append(f"{attr_name}='example_id'" if attr_typ == "str" else f"{attr_name}=1")

        for child in ct.content.iter_elements():
            child_name = child.local_name
            if not child_name:
                continue
            child_camel = snake_to_camel(child_name)
            opt = child.min_occurs == 0
            is_list = child.max_occurs is None or child.max_occurs > 1
            t = f'List["{child_camel}"]' if is_list else f'"{child_camel}"'
            arg = f"{child_name}: {'Optional[' + t + ']' if opt else t}"
            fields.append(arg)
            assigns.append(f"        self.{child_name} = {child_name}")
            child_ns_prefix, child_tag = split_ns_name(child.name, ns_map)
            child_ns = ns_map.get(child_ns_prefix, target_ns)
            if isinstance(child.type, XsdSimpleType):
                if is_list:
                    children.append(textwrap.indent(f"""\
if obj.{child_name}:
    for item in obj.{child_name}:
        XmlAdapter.append_child(el, '{child_tag}', str(item))""", "        "))
                    child_arg = generate_test_args(child, ns_map, target_ns)
                    example_args.append(f"{child_name}=[{child_arg}]")
                else:
                    cond = f"if obj.{child_name}: " if opt else ""
                    children.append(textwrap.indent(
                        f"""{cond}XmlAdapter.append_child(el, '{child_tag}', str(obj.{child_name}))""",
                        "        "))
                    child_arg = generate_test_args(child, ns_map, target_ns)
                    example_args.append(f"{child_name}={child_arg}")
            elif isinstance(child.type, XsdComplexType):
                if is_list:
                    children.append(textwrap.indent(f"""\
if obj.{child_name}:
    for item in obj.{child_name}:
        el.append({child_camel}XmlBuilder().build(item))""", "        "))
                    child_arg = generate_test_args(child, ns_map, target_ns)
                    example_args.append(f"{child_name}=[{child_arg}]")
                else:
                    cond = f"if obj.{child_name}: " if opt else ""
                    children.append(
                        textwrap.indent(f"""{cond}el.append({child_camel}XmlBuilder().build(obj.{child_name}))""",
                                        "        "))
                    child_arg = generate_test_args(child, ns_map, target_ns)
                    example_args.append(f"{child_name}={child_arg}")

        out["complex"].append(
            TEMPLATE_COMPLEX.format(
                classname=classname,
                doc=doc,
                ctor_args=", ".join(fields),
                assigns="\n".join(assigns)
            )
        )
        out["builders"].append(
            TEMPLATE_BUILDER.format(
                classname=classname,
                tag=tag,
                ns=ns,
                attrib="",
                children="\n".join(attribs + children)
            )
        )
        out["tests"].append(
            TEMPLATE_TEST_COMPLEX.format(
                tag=tag,
                classname=classname,
                example_args=", ".join(example_args),
                schema_path=f'{subschema_path}/{elem.local_name}.xsd'
            )
        )


def gen():
    import sys
    subschema_path = sys.argv[1]
    schema = XMLSchema(sys.argv[2])
    out = {"simple": [], "complex": [], "builders": [], "tests": []}
    ns_map = schema.namespaces
    target_ns = schema.target_namespace
    processed = set()

    for sch in schema.elements.values():
        for elem in sch.iter_components():
            if isinstance(elem, XsdElement):
                process_element(elem, ns_map, out, subschema_path, processed, target_ns)

    base = Path("generated")
    base.mkdir(exist_ok=True)
    (base / "types.py").write_text(
        "import re\nfrom typing import Optional, List, Literal\n\n" +
        "\n".join(out["simple"]) + "\n" + "\n".join(out["complex"]),
        encoding='utf-8'
    )
    (base / "builders.py").write_text(
        "import xml.etree.ElementTree as ET\nfrom .types import *\nfrom typing import Dict, Optional\nfrom abc import ABC, abstractmethod\n\n" +
        "class XmlBuilderInterface(ABC):\n    @abstractmethod\n    def build(self, obj) -> ET.Element: ...\n\n" +
        "class XmlAdapter:\n    @staticmethod\n    def create_element(tag: str, text: Optional[str]=None, attrib: Optional[Dict[str,str]]=None)->ET.Element:\n" +
        "        el=ET.Element(tag, attrib=attrib or {})\n        if text is not None: el.text=text\n        return el\n\n" +
        "    @staticmethod\n    def append_child(parent: ET.Element, tag:str, text:Optional[str]=None, attrib:Optional[Dict[str,str]]=None)->ET.Element:\n" +
        "        ch=XmlAdapter.create_element(tag,text,attrib)\n        parent.append(ch)\n        return ch\n\n" +
        "\n".join(out["builders"]),
        encoding='utf-8'
    )
    (base / "test_builders.py").write_text(
        "import unittest\nimport xml.etree.ElementTree as ET\nfrom lxml import etree as LET\nfrom xml.dom import minidom\nfrom .types import *\nfrom .builders import *\n\nclass TestXmlValidation(unittest.TestCase):\n" +
        "    def validar_xml(self,obj,builder,subschema_path):\n" +
        "        xml_el=builder.build(obj)\n" +
        "        xml_str=ET.tostring(xml_el,encoding='utf-8')\n" +
        "        print(minidom.parseString(xml_str).toprettyxml(indent='  '))\n" +
        "        schema_doc = LET.parse(subschema_path)\n" +
        "        schema = LET.XMLSchema(schema_doc)\n" +
        "        doc = LET.fromstring(xml_str)\n" +
        "        ok = schema.validate(doc)\n" +
        "        if not ok: print(schema.error_log)\n" +
        "        self.assertTrue(ok)\n\n" +
        "\n".join(out["tests"]),
        encoding='utf-8'
    )


if __name__ == "__main__":
    gen()