import unittest
from lxml import etree as LET
from xml.dom import minidom
from source.cadastro_intermediario.builders import *

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


    def test_evtCadIntermediario(self):
        # Criar um objeto Evtcadintermediario de exemplo
        obj = Evtcadintermediario(id='example_id', ideEvento=Ideevento(indRetificacao=Indretificacao.from_str('1'), nrRecibo=Nrrecibo.from_str('example'), tpAmb=Tpamb.from_str('1'), aplicEmi=Aplicemi.from_str('1'), verAplic=Veraplic.from_str('example')), ideDeclarante=Idedeclarante(cnpjDeclarante=Cnpjdeclarante.from_str('12345678000195')), infoIntermediario=Infointermediario(GIIN=Giin.from_str('example'), tpNI=Tpni.from_str('1'), NIIntermediario=Niintermediario.from_str('example'), nomeIntermediario=Nomeintermediario.from_str('Teste Nome'), endereco=Endereco(enderecoLivre=Enderecolivre.from_str('Rua Exemplo'), municipio=Municipio.from_str('Sao Paulo'), pais=Pais.from_str('BR')), paisResidencia=Paisresidencia.from_str('BR')))
        builder = EvtcadintermediarioXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-intermediario/evtCadIntermediario.xsd")


    def test_ideEvento(self):
        # Criar um objeto Ideevento de exemplo
        obj = Ideevento(indRetificacao=Indretificacao.from_str('1'), nrRecibo=Nrrecibo.from_str('example'), tpAmb=Tpamb.from_str('1'), aplicEmi=Aplicemi.from_str('1'), verAplic=Veraplic.from_str('example'))
        builder = IdeeventoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-intermediario/ideEvento.xsd")


    def test_ideDeclarante(self):
        # Criar um objeto Idedeclarante de exemplo
        obj = Idedeclarante(cnpjDeclarante=Cnpjdeclarante.from_str('12345678000195'))
        builder = IdedeclaranteXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-intermediario/ideDeclarante.xsd")


    def test_infoIntermediario(self):
        # Criar um objeto Infointermediario de exemplo
        obj = Infointermediario(GIIN=Giin.from_str('example'), tpNI=Tpni.from_str('1'), NIIntermediario=Niintermediario.from_str('example'), nomeIntermediario=Nomeintermediario.from_str('Teste Nome'), endereco=Endereco(enderecoLivre=Enderecolivre.from_str('Rua Exemplo'), municipio=Municipio.from_str('Sao Paulo'), pais=Pais.from_str('BR')), paisResidencia=Paisresidencia.from_str('BR'))
        builder = InfointermediarioXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-intermediario/infoIntermediario.xsd")


    def test_endereco(self):
        # Criar um objeto Endereco de exemplo
        obj = Endereco(enderecoLivre=Enderecolivre.from_str('Rua Exemplo'), municipio=Municipio.from_str('Sao Paulo'), pais=Pais.from_str('BR'))
        builder = EnderecoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/cadastro-intermediario/endereco.xsd")

