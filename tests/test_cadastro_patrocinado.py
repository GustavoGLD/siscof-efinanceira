import unittest
from lxml import etree as LET
from xml.dom import minidom
from source.cadastrar_patrocinado.builders import *

class TestXmlValidation(unittest.TestCase):
    def validar_xml(self,obj,builder,subschema_path):
        xml_el=builder.build(obj)
        xml_str=ET.tostring(xml_el,encoding='utf-8')
        print(minidom.parseString(xml_str).toprettyxml(indent='  '))
        schema_doc = LET.parse(subschema_path)
        schema = LET.XMLSchema(schema_doc)
        doc = LET.fromstring(xml_str)
        ok = schema.validate(doc)
        if not ok: print(schema.error_log)
        self.assertTrue(ok)

    def test_ideEvento(self):
        # Criar um objeto Ideevento de exemplo
        builder = IdeeventoXmlBuilder()
        obj = Ideevento(
            indRetificacao=Indretificacao.from_str('1'),
            nrRecibo=Nrrecibo.from_str('123456789012345'),
            tpAmb=Tpamb.from_str('1'),
            aplicEmi=Aplicemi.from_str('1'),
            verAplic=Veraplic.from_str('1.0')
        )
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-patrocinado/ideEvento.xsd")


    def test_ideDeclarante(self):
        # Criar um objeto Idedeclarante de exemplo
        obj = Idedeclarante(
            cnpjDeclarante=Cnpjdeclarante.from_str('12345678000195'),
            GIIN=Giin.from_str('1234567890'),
            CategoriaPatrocinador=Categoriapatrocinador.from_str('1')
        )
        builder = IdedeclaranteXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-patrocinado/ideDeclarante.xsd")


    def test_infoPatrocinado(self):
        # Criar um objeto Infopatrocinado de exemplo
        obj = Infopatrocinado(
            GIIN=Giin.from_str('1234567890'),
            CNPJ=Cnpj.from_str('12345678000195'),
            NIF=[Nif(NumeroNIF=Numeronif.from_str('123'), PaisEmissao=Paisemissao.from_str('BR'), tpNIF=Tpnif.from_str('1'))],
            nomePatrocinado=Nomepatrocinado.from_str('Nome Exemplo'),
            tpNome=Tpnome.from_str('1'),
            endereco=EnderecoEntidadePatrocinada(
                enderecoLivre=Enderecolivre.from_str('Rua Exemplo'),
                CEP=Cep.from_str('12345-678'),
                municipio=Municipio.from_str('Sao Paulo'),
                pais=Pais.from_str('BR')
            ),
            tpEndereco=Tpendereco.from_str('Rua Exemplo'),
            EnderecoOutros=[
                Enderecooutros(
                    tpEndereco=Tpendereco.from_str('Rua Exemplo'),
                    EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'),
                    EnderecoEstrutura=Enderecoestrutura(
                        EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'),
                        Endereco=Endereco(
                            Logradouro=Logradouro.from_str('Rua Exemplo'),
                            Numero=Numero.from_str('123'),
                            Complemento=Complemento.from_str('Apto 456'),
                            Andar=Andar.from_str('5'),
                            Bairro=Bairro.from_str('Centro'),
                            CaixaPostal=Caixapostal.from_str('12345')),
                        CEP=Cep.from_str('12345-678'),
                        Municipio=Municipio.from_str('Sao Paulo'),
                        UF=Uf.from_str('SP')
                    ),
                    Pais=Pais.from_str('BR')
                )
            ],
            paisResid=[Paisresid(Pais=Pais.from_str('BR'))]
        )
        builder = InfopatrocinadoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-patrocinado/infoPatrocinado.xsd")


    def test_NIF(self):
        # Criar um objeto Nif de exemplo
        obj = Nif(NumeroNIF=Numeronif.from_str('123'), PaisEmissao=Paisemissao.from_str('BR'), tpNIF=Tpnif.from_str('1'))
        builder = NifXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-patrocinado/NIF.xsd")


    def test_endereco(self):
        # Criar um objeto Endereco de exemplo
        obj = EnderecoEntidadePatrocinada(enderecoLivre=Enderecolivre.from_str('Rua Exemplo'), CEP=Cep.from_str('12345-678'), municipio=Municipio.from_str('Sao Paulo'), pais=Pais.from_str('BR'))
        builder = EnderecoEntidadePatrocinadaXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-patrocinado/endereco2.xsd")


    def test_EnderecoOutros(self):
        # Criar um objeto Enderecooutros de exemplo
        obj = Enderecooutros(tpEndereco=Tpendereco.from_str('Rua Exemplo'), EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), EnderecoEstrutura=Enderecoestrutura(EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), Endereco=Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345')), CEP=Cep.from_str('12345-678'), Municipio=Municipio.from_str('Sao Paulo'), UF=Uf.from_str('SP')), Pais=Pais.from_str('BR'))
        builder = EnderecooutrosXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-patrocinado/EnderecoOutros.xsd")


    def test_EnderecoEstrutura(self):
        # Criar um objeto Enderecoestrutura de exemplo
        obj = Enderecoestrutura(EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), Endereco=Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345')), CEP=Cep.from_str('12345-678'), Municipio=Municipio.from_str('Sao Paulo'), UF=Uf.from_str('SP'))
        builder = EnderecoestruturaXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-patrocinado/EnderecoEstrutura.xsd")


    def test_Endereco(self):
        # Criar um objeto Endereco de exemplo
        obj = Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345'))
        builder = EnderecoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-patrocinado/endereco.xsd")


    def test_paisResid(self):
        # Criar um objeto Paisresid de exemplo
        obj = Paisresid(Pais=Pais.from_str('BR'))
        builder = PaisresidXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-patrocinado/paisResid.xsd")
