import unittest
from xml.dom import minidom
from xml.etree import ElementTree as ET

from lxml import etree as LET

from source.abertura import *


class TestXmlValidation(unittest.TestCase):
    def test_telefone(self):
        # Instancia o telefone
        telefone = Telefone(
            ddd=DDD.from_str("11"),
            numero=NumeroTel.from_str("987654321"),
            ramal=Ramal.from_str("123")
        )

        # Gera XML
        builder = TelefoneXmlBuilder()
        xml_element = builder.build(telefone)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))

        # Carrega o XSD
        with open("../schemas/subschemas/abertura/telefone.xsd", "rb") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)

        # Valida XML
        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")

        # Debug em caso de falha
        if not schema.validate(doc):
            print(schema.error_log)

    def test_endereco(self):
        endereco = Endereco(
            logradouro=Logradouro.from_str("Rua das Flores"),
            numero=Numero.from_str("123"),
            complemento=Complemento.from_str("Apto 45"),
            bairro=Bairro.from_str("Centro"),
            cep=CEP.from_str("12345678"),
            municipio=Municipio.from_str("São Paulo"),
            uf=UF.from_str("SP")
        )

        # Gera XML
        builder = EnderecoXmlBuilder()
        xml_element = builder.build(endereco)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))

        # Carrega o XSD
        with open("../schemas/subschemas/abertura/Endereço.xsd", "rb") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)

        # Valida XML
        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")

        # Debug em caso de falha
        if not schema.validate(doc):
            print(schema.error_log)

    def test_respefin(self):
        respefin = ResponsavelEFinanceira(
            nome=Nome("João da Silva"),
            cpf=CPF("12345678901"),
            telefone=Telefone(
                ddd=DDD("11"),
                numero=NumeroTel("987654321"),
                ramal=Ramal("123")
            ),
            setor=Setor("Financeiro"),
            email=Email("joao@gmail.com"),
            endereco=Endereco(
                logradouro=Logradouro("Rua das Flores"),
                numero=Numero("123"),
                complemento=Complemento("Apto 45"),
                bairro=Bairro("Centro"),
                cep=CEP("12345678"),
                municipio=Municipio("São Paulo"),
                uf=UF("SP")
            )
        )

        # Gera XML
        builder = RespeFinXmlBuilder()
        xml_element = builder.build(respefin)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))

        # Carrega o XSD
        with open("../schemas/subschemas/abertura/RespeFin.xsd", "rb") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)

        # Valida XML
        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")

        # Debug em caso de falha
        if not schema.validate(doc):
            print(schema.error_log)

    def test_responsavelrmf(self):
        responsavel_rmf = ResponsavelRMF(
            nome=Nome("Maria da Silva"),
            cpf=CPF("12345678901"),
            telefone=Telefone(
                ddd=DDD("11"),
                numero=NumeroTel("987654321"),
                ramal=Ramal("123")
            ),
            setor=Setor("Financeiro"),
            endereco=Endereco(
                logradouro=Logradouro("Rua das Flores"),
                numero=Numero("123"),
                complemento=Complemento("Apto 45"),
                bairro=Bairro("Centro"),
                cep=CEP("12345678"),
                municipio=Municipio("São Paulo"),
                uf=UF("SP")
            ),
            cnpj=CNPJ.from_str("12345678000195")
        )

        # Gera XML
        builder = ResponsavelRMFXmlBuilder()
        xml_element = builder.build(responsavel_rmf)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))

        # Carrega o XSD
        with open("../schemas/subschemas/abertura/ResponsavelRMF.xsd", "rb") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)

        # Valida XML
        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")

        # Debug em caso de falha
        if not schema.validate(doc):
            print(schema.error_log)

    def test_RepresLegal(self):
        repres_legal = RepresLegal(
            #nome=Nome("Carlos da Silva"),
            setor=Setor("Jurídico"),
            cpf=CPF("12345678901"),
            telefone=Telefone(
                ddd=DDD("11"),
                numero=NumeroTel("987654321"),
                ramal=Ramal("123")
            )
        )

        # Gera XML
        builder = RepresLegalXmlBuilder()
        xml_element = builder.build(repres_legal)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))

        # Carrega o XSD
        with open("../schemas/subschemas/abertura/RepresLegal.xsd", "rb") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)

        # Valida XML
        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")

        # Debug em caso de falha
        if not schema.validate(doc):
            print(schema.error_log)

    def test_abertura_mov_op_fin(self):
        abertura_mov_op_fin = AberturaMovOpFin(
            repres_legal=RepresLegal(
                # nome=Nome("Carlos da Silva"),
                setor=Setor("Jurídico"),
                cpf=CPF("12345678901"),
                telefone=Telefone(
                    ddd=DDD("11"),
                    numero=NumeroTel("987654321"),
                    ramal=Ramal("123")
                )
            ),
            responsavel_rmf=ResponsavelRMF(
                nome=Nome("Maria da Silva"),
                cpf=CPF("12345678901"),
                telefone=Telefone(
                    ddd=DDD("11"),
                    numero=NumeroTel("987654321"),
                    ramal=Ramal("123")
                ),
                setor=Setor("Financeiro"),
                endereco=Endereco(
                    logradouro=Logradouro("Rua das Flores"),
                    numero=Numero("123"),
                    complemento=Complemento("Apto 45"),
                    bairro=Bairro("Centro"),
                    cep=CEP("12345678"),
                    municipio=Municipio("São Paulo"),
                    uf=UF("SP")
                ),
                cnpj=CNPJ.from_str("12345678000195")
            ),
            respe_fin=ResponsavelEFinanceira(
                nome=Nome("João da Silva"),
                cpf=CPF("12345678901"),
                telefone=Telefone(
                    ddd=DDD.from_str("11"),
                    numero=NumeroTel.from_str("987654321"),
                    ramal=None
                ),
                setor=Setor.from_str("Financeiro"),
                email=Email("gustavo@gmail.com"),
                endereco=Endereco(
                    logradouro=Logradouro.from_str("Rua das Flores"),
                    numero=Numero.from_str("123"),
                    complemento=Complemento.from_str("Apto 45"),
                    bairro=Bairro.from_str("Centro"),
                    cep=CEP.from_str("12345678"),
                    municipio=Municipio.from_str("São Paulo"),
                    uf=UF.from_str("SP")
                )
            )
        )

        # Gera XML
        builder = AberturaMovOpFinXmlBuilder()
        xml_element = builder.build(abertura_mov_op_fin)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))
        # Carrega o XSD
        with open("../schemas/subschemas/abertura/AberturaMovOpFin.xsd", "rb") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)
        # Valida XML
        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")
        # Debug em caso de falha
        if not schema.validate(doc):
            print(schema.error_log)

    def test_info_abertura(self):
        info_abertura = InfoAbertura(
            dt_inicio=DtInicio.from_str("2023-01-01"),
            dt_fim=DtFim.from_str("2023-06-30")
        )

        # Gera XML
        builder = InfoAberturaXmlBuilder()
        xml_element = builder.build(info_abertura)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))

        # Carrega o XSD
        with open("../schemas/subschemas/abertura/infoAbertura.xsd", "rb") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)

        # Valida XML
        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")

        # Debug em caso de falha
        if not schema.validate(doc):
            print(schema.error_log)

    def test_ide_declarante(self):
        ide_declarante = IdentificacaoEntidadeDeclarante(
            cnpj_declarante=CnpjDeclarante.from_str("12345678000195")
        )

        # Gera XML
        builder = IdeDeclanteXmlBuilder()
        xml_element = builder.build(ide_declarante)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))

        # Carrega o XSD
        with open("../schemas/subschemas/abertura/ideDeclarante.xsd", "rb") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)

        # Valida XML
        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")

        # Debug em caso de falha
        if not schema.validate(doc):
            print(schema.error_log)

    def test_evt_abertura_e_financeira(self):
        evt_abertura = EvtAberturaeFinanceira(
            _id=ID("ID123456789012345678"),
            ide_evento=IdentificaoEvento(
                ind_retificacao=IndRetificacao.identificar_como_original(),
                aplic_emi=TipoAplicativoEmissor.aplicativo_de_terceiros(),
                ver_aplic=VerAplic("1.0"),
                nr_recibo=NumeroRecibo.from_str("12345-12-345-6789-67890"),
                tp_amb=TipoDeAmbiente.ambiente_de_testes()
            ),
            ide_declarante=IdentificacaoEntidadeDeclarante(
                cnpj_declarante=CnpjDeclarante.from_str("12345678000195")
            ),
            info_abertura=InfoAbertura(
                dt_inicio=DtInicio.from_str("2023-01-01"),
                dt_fim=DtFim.from_str("2023-06-30")
            ),
            abertura_mov_op_fin=AberturaMovOpFin(
                repres_legal=RepresLegal(
                    # nome=Nome("Carlos da Silva"),
                    setor=Setor("Jurídico"),
                    cpf=CPF("12345678901"),
                    telefone=Telefone(
                        ddd=DDD("11"),
                        numero=NumeroTel("987654321"),
                        ramal=Ramal("123")
                    )
                ),
                responsavel_rmf=ResponsavelRMF(
                    nome=Nome("Maria da Silva"),
                    cpf=CPF("12345678901"),
                    telefone=Telefone(
                        ddd=DDD("11"),
                        numero=NumeroTel("987654321"),
                        ramal=Ramal("123")
                    ),
                    setor=Setor("Financeiro"),
                    endereco=Endereco(
                        logradouro=Logradouro("Rua das Flores"),
                        numero=Numero("123"),
                        complemento=Complemento("Apto 45"),
                        bairro=Bairro("Centro"),
                        cep=CEP("12345678"),
                        municipio=Municipio("São Paulo"),
                        uf=UF("SP")
                    ),
                    cnpj=CNPJ.from_str("12345678000195")
                ),
                respe_fin=ResponsavelEFinanceira(
                    nome=Nome("João da Silva"),
                    cpf=CPF("12345678901"),
                    telefone=Telefone(
                        ddd=DDD.from_str("11"),
                        numero=NumeroTel.from_str("987654321"),
                        ramal=None
                    ),
                    setor=Setor.from_str("Financeiro"),
                    email=Email("gustavo@gmail.com"),
                    endereco=Endereco(
                        logradouro=Logradouro.from_str("Rua das Flores"),
                        numero=Numero.from_str("123"),
                        complemento=Complemento.from_str("Apto 45"),
                        bairro=Bairro.from_str("Centro"),
                        cep=CEP.from_str("12345678"),
                        municipio=Municipio.from_str("São Paulo"),
                        uf=UF.from_str("SP")
                    )
                )
            )
        )

        # Gera XML
        builder = EvtAberturaeFinanceiraXmlBuilder()
        xml_element = builder.build(evt_abertura)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))

        # Carrega o XSD
        with open("../schemas/subschemas/abertura/evtAberturaeFinanceira.xsd", "rb") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)

        # Valida XML
        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")

        # Debug em caso de falha
        if not schema.validate(doc):
            print(schema.error_log)
