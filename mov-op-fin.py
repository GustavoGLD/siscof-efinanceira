import re
import textwrap
from xmlschema import XMLSchema, XsdElement
from xmlschema.validators import XsdSimpleType, XsdAtomicBuiltin, XsdComplexType
from pathlib import Path
from typing import Dict, Optional, Set
import unicodedata

# Templates para geração de código
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
        el = XmlAdapter.create_element("{{{ns}}}{tag}"{attrib})
{children}
        return el
"""

TEMPLATE_TEST = """
    def test_{tag}(self):
        # Criar um objeto {classname} de exemplo
        obj = {classname}({example_args})
        builder = {classname}XmlBuilder()
        self.validar_xml(obj, builder, "{schema_path}")
"""

# Mapeamento de tipos XML para Python
TYPE_MAPPING = {
    str: "str",
    int: "int",
    float: "float",
    bool: "bool",
    "xs:string": "str",
    "xs:unsignedInt": "int",
    "xs:ID": "str",
}

# Função para converter snake_case para CamelCase
def snake_to_camel(s):
    return ''.join(p.capitalize() for p in s.split('_'))

# Função para extrair namespace e nome do elemento
def split_ns_name(elem_name: str, ns_map: Dict[str, str]) -> tuple[str, str]:
    if "}" in elem_name:
        ns, name = elem_name.split("}")
        ns = ns[1:]  # Remove '{'
        prefix = next((k for k, v in ns_map.items() if v == ns), "")
        return prefix, name
    return "", elem_name

# Função para sanitizar strings
def sanitize_string(text: str) -> str:
    # Normalizar para decompor caracteres acentuados (e.g., 'é' -> 'e')
    text = unicodedata.normalize('NFKD', text)
    # Converter para ASCII, ignorando caracteres não-ASCII
    text = text.encode('ascii', 'ignore').decode('ascii')
    # Substituir quebras de linha e tabs por espaços
    text = re.sub(r'\s+', ' ', text.strip())
    return text

# Função auxiliar para gerar argumentos de teste para um elemento
def generate_test_args(elem: XsdElement, ns_map: Dict[str, str], target_ns: str) -> str:
    if isinstance(elem.type, XsdSimpleType):
        # Para simpleType, usar from_str com um valor de exemplo
        tipo: XsdAtomicBuiltin = elem.type.primitive_type
        python_type = tipo.python_type
        typ = TYPE_MAPPING.get(python_type, "str")
        example_value = "1" if typ == "int" else "example"
        if elem.type.facets.get("pattern"):
            pattern = elem.type.facets["pattern"].pattern
            if pattern == "[1|2|3]":
                example_value = "1"
            elif pattern == "[0-9]{1,18}[-][0-9]{2}[-][0-9]{3}[-][0-9]{4}[-][0-9]{1,18}":
                example_value = "123-12-123-1234-123"
            elif pattern == "[1|2]":
                example_value = "1"
        return f"{snake_to_camel(elem.local_name)}.from_str({example_value!r})"
    elif isinstance(elem.type, XsdComplexType):
        if not hasattr(elem.type.content, "iter_elements"):
            return "None"

        # Para complexType, construir instância com argumentos recursivos
        args = []
        # Atributos
        for attr_name, attr in elem.type.attributes.items():
            if attr.use == "required":
                attr_typ = TYPE_MAPPING.get(attr.type.name, "str")
                args.append(f"{attr_name}='example_id'" if attr_typ == "str" else f"{attr_name}=1")
        # Elementos filhos

        print(elem)
        for child in elem.type.content.iter_elements():
            if not isinstance(child.type, XsdElement):
                continue
            child_name = child.local_name
            print(child)
            child_camel = snake_to_camel(child_name)
            is_list = child.max_occurs is None or child.max_occurs > 1
            child_arg = generate_test_args(child, ns_map, target_ns)
            if is_list:
                args.append(f"{child_name}=[{child_arg}]")
            else:
                args.append(f"{child_name}={child_arg}")
        return f"{snake_to_camel(elem.local_name)}({', '.join(args)})"
    return "None"  # Fallback para elementos sem tipo definido (e.g., referências)

# Função para processar um elemento
def process_element(
    elem: XsdElement,
    ns_map: Dict[str, str],
    out: Dict[str, list],
    schema_path: str,
    processed: Set[str],
    target_ns: str
):
    name = elem.local_name
    if name in processed:
        return
    processed.add(name)

    ct = elem.type
    # Extrair documentação de forma segura
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
        # Tipo simples
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
        out["builders"].append(
            TEMPLATE_BUILDER.format(
                classname=classname,
                tag=tag,
                ns=ns,
                attrib="",
                children="        el.text = str(obj.value)"
            )
        )
        # Exemplo para teste
        example_value = "1" if typ == "int" else "example"
        if ct.facets.get("pattern"):
            pattern = ct.facets["pattern"].pattern
            if pattern == "[1|2|3]":
                example_value = "1"
            elif pattern == "[0-9]{1,18}[-][0-9]{2}[-][0-9]{3}[-][0-9]{4}[-][0-9]{1,18}":
                example_value = "123-12-123-1234-123"
            elif pattern == "[1|2]":
                example_value = "1"
        out["tests"].append(
            TEMPLATE_TEST.format(
                tag=tag,
                classname=classname,
                example_args=f"{example_value!r}",
                schema_path=schema_path
            )
        )
    elif isinstance(ct, XsdComplexType):
        # Tipo complexo
        fields, assigns, children, example_args, attribs = [], [], [], [], []
        # Atributos
        for attr_name, attr in ct.attributes.items():
            if attr.use == "required":
                attr_typ = TYPE_MAPPING.get(attr.type.name, "str")
                fields.append(f"{attr_name}: {attr_typ}")
                assigns.append(f"        self.{attr_name} = {attr_name}")
                attribs.append(f"        el.set('{attr_name}', str(obj.{attr_name}))")
                example_args.append(f"{attr_name}='example_id'" if attr_typ == "str" else f"{attr_name}=1")

        # Elementos filhos
        for child in ct.content.iter_elements():
            child_name = child.local_name
            child_camel = snake_to_camel(child_name)
            opt = child.min_occurs == 0
            is_list = child.max_occurs is None or child.max_occurs > 1
            t = f"List[{child_camel}]" if is_list else child_camel
            arg = f"{child_name}: {'Optional['+t+']' if opt else t}"
            fields.append(arg)
            assigns.append(f"        self.{child_name} = {child_name}")
            # Builder para filho
            child_ns_prefix, child_tag = split_ns_name(child.name, ns_map)
            child_ns = ns_map.get(child_ns_prefix, target_ns)
            if is_list:
                children.append(textwrap.indent(f"""\
if obj.{child_name}:
    for item in obj.{child_name}:
        el.append({child_camel}XmlBuilder().build(item))""", "        "))
                child_arg = generate_test_args(child, ns_map, target_ns)
                example_args.append(f"{child_name}=[{child_arg}]")
            else:
                cond = f"if obj.{child_name}: " if opt else ""
                children.append(textwrap.indent(f"""{cond}el.append({child_camel}XmlBuilder().build(obj.{child_name}))""", "        "))
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
            TEMPLATE_TEST.format(
                tag=tag,
                classname=classname,
                example_args=", ".join(example_args),
                schema_path=schema_path
            )
        )

# Função principal de geração
def gen():
    schema_path = "schemas/evtMovOpFin-v1_2_1.xsd"
    schema = XMLSchema(schema_path)
    out = {"simple": [], "complex": [], "builders": [], "tests": []}
    ns_map = schema.namespaces
    target_ns = schema.target_namespace
    processed = set()

    # Processar todos os elementos de nível superior e seus componentes
    for sch in schema.elements.values():
        for elem in sch.iter_components():
            if isinstance(elem, XsdElement):
                process_element(elem, ns_map, out, schema_path, processed, target_ns)

    # Salvar arquivos com codificação UTF-8 explícita
    base = Path("generated")
    base.mkdir(exist_ok=True)
    (base/"types.py").write_text(
        "import re\nfrom typing import Optional, List, Literal\n\n" +
        "\n".join(out["simple"]) + "\n" + "\n".join(out["complex"]),
        encoding='utf-8'
    )
    (base/"builders.py").write_text(
        "import xml.etree.ElementTree as ET\nfrom .types import *\nfrom typing import Dict, Optional\nfrom abc import ABC, abstractmethod\n\n" +
        "class XmlBuilderInterface(ABC):\n    @abstractmethod\n    def build(self, obj) -> ET.Element: ...\n\n" +
        "class XmlAdapter:\n    @staticmethod\n    def create_element(tag: str, text: Optional[str]=None, attrib: Optional[Dict[str,str]]=None)->ET.Element:\n" +
        "        el=ET.Element(tag, attrib=attrib or {})\n        if text is not None: el.text=text\n        return el\n\n" +
        "    @staticmethod\n    def append_child(parent: ET.Element, tag:str, text:Optional[str]=None, attrib:Optional[Dict[str,str]]=None)->ET.Element:\n" +
        "        ch=XmlAdapter.create_element(tag,text,attrib)\n        parent.append(ch)\n        return ch\n\n" +
        "\n".join(out["builders"]),
        encoding='utf-8'
    )
    (base/"test_builders.py").write_text(
        "import unittest\nimport xml.etree.ElementTree as ET\nfrom lxml import etree as LET\nfrom xml.dom import minidom\nfrom .types import *\nfrom .builders import *\n\nclass TestXmlValidation(unittest.TestCase):\n" +
        "    def validar_xml(self,obj,builder,schema_path):\n" +
        "        xml_el=builder.build(obj)\n" +
        "        xml_str=ET.tostring(xml_el,encoding='utf-8')\n" +
        "        print(minidom.parseString(xml_str).toprettyxml(indent='  '))\n" +
        "        schema_doc = LET.parse(schema_path)\n" +
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