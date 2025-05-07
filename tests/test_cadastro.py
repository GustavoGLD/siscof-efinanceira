import unittest
from xml.dom import minidom
from xml.etree import ElementTree as ET

from lxml import etree as LET

from source.cadastro import *


class TestXmlValidation(unittest.TestCase):
    def validar_xml(self, objeto, builder, schema_path):
        xml_element = builder.build(objeto)
        xml_str = ET.tostring(xml_element, encoding="utf-8")
        print(minidom.parseString(xml_str).toprettyxml(indent="  "))

        with open(schema_path, "r") as f:
            schema_doc = LET.parse(f)
        schema = LET.XMLSchema(schema_doc)

        doc = LET.fromstring(xml_str)
        self.assertTrue(schema.validate(doc), f"\n{str(schema.error_log)}")

        if not schema.validate(doc):
            print(schema.error_log)

    def test_Endereco(self):
        # Teste de criação de um objeto Endereco
        endereco = Endereco(
            logradouro=Logradouro("Rua Exemplo"),
            numero=Numero("123"),
            complemento=Complemento("Apto 456"),
            andar=Andar("5"),
            bairro=Bairro("Centro"),
            caixa_postal=CaixaPostal("123456")
        )

        builder = EnderecoXmlBuilder()
        self.validar_xml(endereco, builder, "../schemas/subschemas/cadastro/Endereco.xsd")

    def test_EnderecoEstrutura(self):
        # Teste de criação de um objeto EnderecoEstrutura
        endereco_estrutura = EnderecoOutrosEnderecoEstrutura(
            endereco_estrutura_endereco_livre=EnderecoEstruturaEnderecoLivre("Rua Exemplo"),
            endereco=Endereco(
                logradouro=Logradouro("Rua Exemplo"),
                numero=Numero("123"),
                complemento=Complemento("Apto 456"),
                andar=Andar("5"),
                bairro=Bairro("Centro"),
                caixa_postal=CaixaPostal("123456")
            ),
            endereco_estrutura_cep=EnderecoEstruturaCEP("12345678"),
            endereco_estrutura_municipio=EnderecoEstruturaMunicipio("São Paulo"),
            endereco_estrutura_uf=EnderecoEstruturaUF("SP")
        )

        builder = EnderecoOutrosEnderecoEstruturaXmlBuilder()
        self.validar_xml(endereco_estrutura, builder, "../schemas/subschemas/cadastro/EnderecoEstrutura.xsd")

    def test_EnderecoOutros(self):
        # Teste de criação de um objeto EnderecoOutros
        endereco_outros = EnderecoOutros1(
            endereco_outros_pais=PaisResidSigla('BR'),
            endereco_outros_tp_endereco=EnderecoOutrosTpEndereco("1"),
            #endereco_outros_endereco_livre=EnderecoOutrosEnderecoLivre("Rua Exemplo"),
            endereco_outros_endereco_estrutura=EnderecoOutrosEnderecoEstrutura(
                endereco_estrutura_endereco_livre=EnderecoEstruturaEnderecoLivre("Rua Exemplo"),
                endereco=Endereco(
                    logradouro=Logradouro("Rua Exemplo"),
                    numero=Numero("123"),
                    complemento=Complemento("Apto 456"),
                    andar=Andar("5"),
                    bairro=Bairro("Centro"),
                    caixa_postal=CaixaPostal("123456")
                ),
                endereco_estrutura_cep=EnderecoEstruturaCEP("12345678"),
                endereco_estrutura_municipio=EnderecoEstruturaMunicipio("São Paulo"),
                endereco_estrutura_uf=EnderecoEstruturaUF("SP")
            )
        )

        builder = EnderecoOutros1XmlBuilder()
        self.validar_xml(endereco_outros, builder, "../schemas/subschemas/cadastro/EnderecoOutros.xsd")

    def test_ideDeclarante(self):
        ide_declarante = IdeDeclarante(
            cnpj_declarante=CnpjDeclarante.from_str("12345678000195")
        )

        builder = IdeDeclaranteXmlBuilder()
        self.validar_xml(ide_declarante, builder, "../schemas/subschemas/cadastro/ideDeclarante.xsd")

    def test_ideEvento(self):
        ide_evento = IdeEvento(
            ind_retificacao=IndRetificacao.identificar_como_original(),
            tp_amb=TpAmb.from_str("1"),
            aplic_emi=TipoAplicativoEmissor.from_str("1"),
            ver_aplic=VerAplic.from_str("1.0"),
            nr_recibo=NumeroRecibo.from_str("12345-12-345-6789-67890")
        )
        builder = IdeEventoXmlBuilder()
        self.validar_xml(ide_evento, builder, "../schemas/subschemas/cadastro/ideEvento.xsd")

    def test_infoTpInstPgto1(self):
        info_tp_inst_pgto1 = InfoTpInstPgto1(
            tp_inst_pgto=TpInstPgto("1")
        )
        builder = InfoTpInstPgto1XmlBuilder()
        self.validar_xml(info_tp_inst_pgto1, builder, "../schemas/subschemas/cadastro/infoTpInstPgto.xsd")

    def test_InfoCadastro(self):
        info_cadastro = InfoCadastro(
            nome=Nome.from_str("Nome da Entidade Declarante"),
            endereco_livre=EnderecoLivre.from_str("Rua Exemplo"),
            municipio=Municipio.from_int(1234567),
            uf=UF.from_str("SP"),
            cep=CEP.from_str("12345678"),
            pais=Pais.from_str("BR"),
            pais_resid1=PaisResid1(PaisResidSigla("BR")),
        )
        builder = InfoCadastroXmlBuilder()
        self.validar_xml(info_cadastro, builder, "../schemas/subschemas/cadastro/infoCadastro.xsd")

    def test_paisResid(self):
        pais_resid1 = PaisResid1(
            pais_resid_pais=PaisResidSigla.from_str("BR")
        )
        builder = PaisResid1XmlBuilder()
        self.validar_xml(pais_resid1, builder, "../schemas/subschemas/cadastro/paisResid.xsd")

    def test_EvtCadDeclarante(self):
        evt_cad_declarante = EvtCadDeclarante(
            id=ID("ID123456789012345678"),
            ide_evento=IdeEvento(
                ind_retificacao=IndRetificacao.identificar_como_original(),
                tp_amb=TpAmb.from_str("1"),
                aplic_emi=TipoAplicativoEmissor.from_str("1"),
                ver_aplic=VerAplic.from_str("1.0")
            ),
            ide_declarante=IdeDeclarante(
                cnpj_declarante=CnpjDeclarante.from_str("12345678000195")
            ),
            info_cadastro=InfoCadastro(
                nome=Nome.from_str("Nome da Entidade Declarante"),
                endereco_livre=EnderecoLivre.from_str("Rua Exemplo"),
                municipio=Municipio.from_int(1234567),
                uf=UF.from_str("SP"),
                cep=CEP.from_str("12345678"),
                pais=Pais.from_str("BR"),
                pais_resid1=PaisResid1(PaisResidSigla("BR")),
            ),
        )
        builder = EvtCadDeclaranteXmlBuilder()
        self.validar_xml(evt_cad_declarante, builder, "../schemas/subschemas/cadastro/evtCadDeclarante.xsd")

    def test_NIF1(self):
        nif1 = NIF1(
            numero_nif=NumeroNIF.from_str("123456789"),
            pais_emissao=PaisEmissao.from_str("BR"),
            tp_nif=TpNIF.from_str("1")
        )
        builder = NIF1XmlBuilder()
        self.validar_xml(nif1, builder, "../schemas/subschemas/cadastro/NIF.xsd")
