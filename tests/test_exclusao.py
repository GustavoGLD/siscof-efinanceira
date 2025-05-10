import unittest
from lxml import etree as LET
from xml.dom import minidom
from source.exclusao.builders import *

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


    def test_evtExclusao(self):
        # Criar um objeto Evtexclusao de exemplo
        obj = Evtexclusao(id='example_id', ideEvento=Ideevento(tpAmb=Tpamb.from_str('1'), aplicEmi=Aplicemi.from_str('1'), verAplic=Veraplic.from_str('example')), ideDeclarante=Idedeclarante(cnpjDeclarante=Cnpjdeclarante.from_str('12345678000195')), infoExclusao=Infoexclusao(nrReciboEvento=Nrreciboevento.from_str('example')))
        builder = EvtexclusaoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/exclusao/evtExclusao.xsd")


    def test_ideEvento(self):
        # Criar um objeto Ideevento de exemplo
        obj = Ideevento(tpAmb=Tpamb.from_str('1'), aplicEmi=Aplicemi.from_str('1'), verAplic=Veraplic.from_str('example'))
        builder = IdeeventoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/exclusao/ideEvento.xsd")


    def test_ideDeclarante(self):
        # Criar um objeto Idedeclarante de exemplo
        obj = Idedeclarante(cnpjDeclarante=Cnpjdeclarante.from_str('12345678000195'))
        builder = IdedeclaranteXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/exclusao/ideDeclarante.xsd")


    def test_infoExclusao(self):
        # Criar um objeto Infoexclusao de exemplo
        obj = Infoexclusao(nrReciboEvento=Nrreciboevento.from_str('example'))
        builder = InfoexclusaoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/exclusao/infoExclusao.xsd")
