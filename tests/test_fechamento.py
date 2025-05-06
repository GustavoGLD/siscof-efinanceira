import unittest
from lxml import etree as LET
from xml.dom import minidom
from source.fechamento.builders import *

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


    def test_evtFechamentoeFinanceira(self):
        # Criar um objeto Evtfechamentoefinanceira de exemplo
        obj = Evtfechamentoefinanceira(id='example_id', ideEvento=Ideevento(indRetificacao=Indretificacao.from_str('1'), nrRecibo=Nrrecibo.from_str('example'), tpAmb=Tpamb.from_str('1'), aplicEmi=Aplicemi.from_str('1'), verAplic=Veraplic.from_str('example')), ideDeclarante=Idedeclarante(cnpjDeclarante=Cnpjdeclarante.from_str('12345678000195')), infoFechamento=Infofechamento(dtInicio=Dtinicio.from_str('2023-01-01'), dtFim=Dtfim.from_str('2023-01-01'), sitEspecial=Sitespecial.from_str('1')), FechamentoPP=Fechamentopp(FechamentoMes=[Fechamentomes(anoMesCaixa=Anomescaixa.from_str('Teste Nome'), quantArqTrans=Quantarqtrans.from_str('1'))]), FechamentoMovOpFin=Fechamentomovopfin(FechamentoMes=[Fechamentomes(anoMesCaixa=Anomescaixa.from_str('Teste Nome'), quantArqTrans=Quantarqtrans.from_str('1'))], EntDecExterior=Entdecexterior(ContasAReportar=Contasareportar.from_str('1')), EntPatDecExterior=[Entpatdecexterior(GIIN=Giin.from_str('example'), CNPJ=Cnpj.from_str('12345678000195'), ContasAReportar=Contasareportar.from_str('1'), inCadPatrocinadoEncerrado=Incadpatrocinadoencerrado.from_str('1'), inGIINEncerrado=Ingiinencerrado.from_str('1'))]), FechamentoMovOpFinAnual=Fechamentomovopfinanual(FechamentoAno=Fechamentoano(anoCaixa=Anocaixa.from_str('12345'), quantArqTrans=Quantarqtrans.from_str('1'))))
        builder = EvtfechamentoefinanceiraXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/evtFechamentoeFinanceira.xsd")


    def test_ideEvento(self):
        # Criar um objeto Ideevento de exemplo
        obj = Ideevento(indRetificacao=Indretificacao.from_str('1'), nrRecibo=Nrrecibo.from_str('example'), tpAmb=Tpamb.from_str('1'), aplicEmi=Aplicemi.from_str('1'), verAplic=Veraplic.from_str('example'))
        builder = IdeeventoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/ideEvento.xsd")


    def test_ideDeclarante(self):
        # Criar um objeto Idedeclarante de exemplo
        obj = Idedeclarante(cnpjDeclarante=Cnpjdeclarante.from_str('12345678000195'))
        builder = IdedeclaranteXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/ideDeclarante.xsd")


    def test_infoFechamento(self):
        # Criar um objeto Infofechamento de exemplo
        obj = Infofechamento(dtInicio=Dtinicio.from_str('2023-01-01'), dtFim=Dtfim.from_str('2023-01-01'), sitEspecial=Sitespecial.from_str('1'))
        builder = InfofechamentoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/infoFechamento.xsd")


    def test_FechamentoPP(self):
        # Criar um objeto Fechamentopp de exemplo
        obj = Fechamentopp(FechamentoMes=[Fechamentomes(anoMesCaixa=Anomescaixa.from_str('Teste Nome'), quantArqTrans=Quantarqtrans.from_str('1'))])
        builder = FechamentoppXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/FechamentoPP.xsd")


    def test_FechamentoMes(self):
        # Criar um objeto Fechamentomes de exemplo
        obj = Fechamentomes(anoMesCaixa=Anomescaixa.from_str('Teste Nome'), quantArqTrans=Quantarqtrans.from_str('1'))
        builder = FechamentomesXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/FechamentoMes.xsd")


    def test_FechamentoMovOpFin(self):
        # Criar um objeto Fechamentomovopfin de exemplo
        obj = Fechamentomovopfin(FechamentoMes=[Fechamentomes(anoMesCaixa=Anomescaixa.from_str('Teste Nome'), quantArqTrans=Quantarqtrans.from_str('1'))], EntDecExterior=Entdecexterior(ContasAReportar=Contasareportar.from_str('1')), EntPatDecExterior=[Entpatdecexterior(GIIN=Giin.from_str('example'), CNPJ=Cnpj.from_str('12345678000195'), ContasAReportar=Contasareportar.from_str('1'), inCadPatrocinadoEncerrado=Incadpatrocinadoencerrado.from_str('1'), inGIINEncerrado=Ingiinencerrado.from_str('1'))])
        builder = FechamentomovopfinXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/FechamentoMovOpFin.xsd")


    def test_EntDecExterior(self):
        # Criar um objeto Entdecexterior de exemplo
        obj = Entdecexterior(ContasAReportar=Contasareportar.from_str('1'))
        builder = EntdecexteriorXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/EntDecExterior.xsd")


    def test_EntPatDecExterior(self):
        # Criar um objeto Entpatdecexterior de exemplo
        obj = Entpatdecexterior(GIIN=Giin.from_str('example'), CNPJ=Cnpj.from_str('12345678000195'), ContasAReportar=Contasareportar.from_str('1'), inCadPatrocinadoEncerrado=Incadpatrocinadoencerrado.from_str('1'), inGIINEncerrado=Ingiinencerrado.from_str('1'))
        builder = EntpatdecexteriorXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/EntPatDecExterior.xsd")


    def test_FechamentoMovOpFinAnual(self):
        # Criar um objeto Fechamentomovopfinanual de exemplo
        obj = Fechamentomovopfinanual(FechamentoAno=Fechamentoano(anoCaixa=Anocaixa.from_str('12345'), quantArqTrans=Quantarqtrans.from_str('1')))
        builder = FechamentomovopfinanualXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/FechamentoMovOpFinAnual.xsd")


    def test_FechamentoAno(self):
        # Criar um objeto Fechamentoano de exemplo
        obj = Fechamentoano(anoCaixa=Anocaixa.from_str('12345'), quantArqTrans=Quantarqtrans.from_str('1'))
        builder = FechamentoanoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/fechamento/FechamentoAno.xsd")
