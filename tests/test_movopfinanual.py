import unittest
import xml.etree.ElementTree as ET
from lxml import etree as LET
from xml.dom import minidom
from source.mov_op_fin_anual.types import *
from source.mov_op_fin_anual.builders import *

class TestXmlValidation(unittest.TestCase):
    def validar_xml(self,obj,builder,subschema_path):
        xml_el=builder.build(obj)
        xml_str=ET.tostring(xml_el,encoding='utf-8')
        print(minidom.parseString(xml_str).toprettyxml(indent='  '))
        #print(pathlib.Path().resolve())
        with open(subschema_path, 'r', encoding="utf-8") as subschema_file:
            subschema_str = subschema_file.read()
            a = LET.fromstring(subschema_str.encode())
            schema = LET.XMLSchema(a)
        #schema_doc = LET.parse(subschema_path)
        #schema = LET.XMLSchema(schema_doc)
        doc = LET.fromstring(xml_str)
        ok = schema.validate(doc)
        if not ok: print(schema.error_log)
        self.assertTrue(ok)

    def test_evtMovOpFinAnual(self):
        # Criar um objeto Evtmovopfinanual de exemplo
        obj = Evtmovopfinanual(id='example_id', ideEvento=Ideevento(indRetificacao=Indretificacao.from_str('1'), nrRecibo=Nrrecibo.from_str('example'), tpAmb=Tpamb.from_str('1'), aplicEmi=Aplicemi.from_str('1'), verAplic=Veraplic.from_str('example')), ideDeclarante=Idedeclarante(cnpjDeclarante=Cnpjdeclarante.from_str('12345678000195')), ideDeclarado=Idedeclarado(tpNI=Tpni.from_str('1'), tpDeclarado=[Tpdeclarado.from_str('example')], NIDeclarado=Nideclarado.from_str('example'), NIF=[Nif(NumeroNIF=Numeronif.from_str('123'), PaisEmissaoNIF=Paisemissaonif.from_str('BR'), tpNIF=Tpnif.from_str('1'))], NomeDeclarado=Nomedeclarado.from_str('Teste Nome'), tpNomeDeclarado=Tpnomedeclarado.from_str('Teste Nome'), NomeOutros=[Nomeoutros(NomePF=Nomepf(tpNome=Tpnome.from_str('Teste Nome'), PrecTitulo=Prectitulo.from_str('example'), Titulo=[Titulo.from_str('example')], PrimeiroNome=Primeironome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), MeioNome=[Meionome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))], PrefixoNome=Prefixonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), UltimoNome=Ultimonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), IdGeracao=[Idgeracao.from_str('example')], Sufixo=[Sufixo.from_str('SP')], GenSufixo=Gensufixo.from_str('SP')), NomePJ=Nomepj(tpNome=Tpnome.from_str('Teste Nome'), Nome=Nome.from_str('Teste Nome')))], DataNasc=Datanasc.from_str('2023-01-01'), InfoNascimento=Infonascimento(Municipio=Municipio.from_str('Sao Paulo'), Bairro=Bairro.from_str('Centro'), PaisNasc=Paisnasc(Pais=Pais.from_str('BR'), AntigoNomePais=Antigonomepais.from_str('Teste Nome'))), EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), tpEndereco=Tpendereco.from_str('Rua Exemplo'), PaisEndereco=Paisendereco(Pais=Pais.from_str('BR')), EnderecoOutros=[Enderecooutros(tpEndereco=Tpendereco.from_str('Rua Exemplo'), EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), EnderecoEstrutura=Enderecoestrutura(EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), Endereco=Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345')), CEP=Cep.from_str('12345-678'), Municipio=Municipio.from_str('Sao Paulo'), UF=Uf.from_str('SP')), Pais=Pais.from_str('BR'))], paisResid=[Paisresid(Pais=Pais.from_str('BR'))], PaisNacionalidade=[Paisnacionalidade(Pais=Pais.from_str('BR'))], Proprietarios=[Proprietarios(tpNI=Tpni.from_str('1'), NIProprietario=Niproprietario.from_str('example'), tpProprietario=Tpproprietario.from_str('example'), NIF=[Nif(NumeroNIF=Numeronif.from_str('123'), PaisEmissaoNIF=Paisemissaonif.from_str('BR'), tpNIF=None)], Nome=Nome.from_str('Teste Nome'), tpNome=Tpnome.from_str('Teste Nome'), NomeOutros=[Nomeoutros(NomePF=Nomepf(tpNome=Tpnome.from_str('Teste Nome'), PrecTitulo=Prectitulo.from_str('example'), Titulo=[Titulo.from_str('example')], PrimeiroNome=Primeironome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), MeioNome=[Meionome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))], PrefixoNome=Prefixonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), UltimoNome=Ultimonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), IdGeracao=[Idgeracao.from_str('example')], Sufixo=[Sufixo.from_str('SP')], GenSufixo=Gensufixo.from_str('SP')), NomePJ=None)], EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), tpEndereco=Tpendereco.from_str('Rua Exemplo'), PaisEndereco=Paisendereco(Pais=Pais.from_str('BR')), EnderecoOutros=[Enderecooutros(tpEndereco=Tpendereco.from_str('Rua Exemplo'), EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), EnderecoEstrutura=Enderecoestrutura(EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), Endereco=Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345')), CEP=Cep.from_str('12345-678'), Municipio=Municipio.from_str('Sao Paulo'), UF=Uf.from_str('SP')), Pais=Pais.from_str('BR'))], paisResid=[Paisresid(Pais=Pais.from_str('BR'))], PaisNacionalidade=[Paisnacionalidade(Pais=Pais.from_str('BR'))], DataNasc=Datanasc.from_str('2023-01-01'), InfoNascimento=Infonascimento(Municipio=Municipio.from_str('Sao Paulo'), Bairro=Bairro.from_str('Centro'), PaisNasc=Paisnasc(Pais=Pais.from_str('BR'), AntigoNomePais=Antigonomepais.from_str('Teste Nome'))), Reportavel=[Reportavel(Pais=Pais.from_str('BR'))])]), Caixa=Caixa(anoCaixa=Anocaixa.from_str('12345'), semestre=Semestre.from_str('1'), movOpFinAnual=Movopfinanual(Conta=[Conta(MedJudic=[Medjudic(NumProcJud=Numprocjud.from_str('example'), Vara=Vara.from_str('1'), SecJud=Secjud.from_str('1'), SubSecJud=Subsecjud.from_str('example'), dtConcessao=Dtconcessao.from_str('2023-01-01'), dtCassacao=Dtcassacao.from_str('2023-01-01'))], infoConta=Infoconta(Reportavel=[Reportavel(Pais=Pais.from_str('BR'))], tpConta=Tpconta.from_str('example'), subTpConta=Subtpconta.from_str('example'), tpNumConta=Tpnumconta.from_str('example'), numConta=Numconta.from_str('example'), tpRelacaoDeclarado=Tprelacaodeclarado.from_str('1'), moeda=Moeda.from_str('example'), Intermediario=Intermediario(GIIN=Giin.from_str('example'), tpNI=Tpni.from_str('1'), NIIntermediario=Niintermediario.from_str('example')), NoTitulares=Notitulares.from_str('example'), dtEncerramentoConta=Dtencerramentoconta.from_str('2023-01-01'), IndInatividade=Indinatividade.from_str('1'), IndNDoc=Indndoc.from_str('1'), Fundo=Fundo(GIIN=Giin.from_str('example'), CNPJ=Cnpj.from_str('12345678000195')), BalancoConta=Balancoconta(vlrUltDia=Vlrultdia.from_str('example')), PgtosAcum=[Pgtosacum(tpPgto=[Tppgto.from_str('example')], totPgtosAcum=Totpgtosacum.from_str('example'))]))])))
        builder = EvtmovopfinanualXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/evtMovOpFinAnual.xsd")


    def test_ideEvento(self):
        # Criar um objeto Ideevento de exemplo
        obj = Ideevento(indRetificacao=Indretificacao.from_str('1'), nrRecibo=Nrrecibo.from_str('example'), tpAmb=Tpamb.from_str('1'), aplicEmi=Aplicemi.from_str('1'), verAplic=Veraplic.from_str('example'))
        builder = IdeeventoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/ideEvento.xsd")


    def test_ideDeclarante(self):
        # Criar um objeto Idedeclarante de exemplo
        obj = Idedeclarante(cnpjDeclarante=Cnpjdeclarante.from_str('12345678000195'))
        builder = IdedeclaranteXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/ideDeclarante.xsd")


    def test_ideDeclarado(self):
        # Criar um objeto Idedeclarado de exemplo
        obj = Idedeclarado(tpNI=Tpni.from_str('1'), tpDeclarado=[Tpdeclarado.from_str('example')], NIDeclarado=Nideclarado.from_str('example'), NIF=[Nif(NumeroNIF=Numeronif.from_str('123'), PaisEmissaoNIF=Paisemissaonif.from_str('BR'), tpNIF=Tpnif.from_str('1'))], NomeDeclarado=Nomedeclarado.from_str('Teste Nome'), tpNomeDeclarado=Tpnomedeclarado.from_str('Teste Nome'), NomeOutros=[Nomeoutros(NomePF=Nomepf(tpNome=Tpnome.from_str('Teste Nome'), PrecTitulo=Prectitulo.from_str('example'), Titulo=[Titulo.from_str('example')], PrimeiroNome=Primeironome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), MeioNome=[Meionome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))], PrefixoNome=Prefixonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), UltimoNome=Ultimonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), IdGeracao=[Idgeracao.from_str('example')], Sufixo=[Sufixo.from_str('SP')], GenSufixo=Gensufixo.from_str('SP')), NomePJ=Nomepj(tpNome=Tpnome.from_str('Teste Nome'), Nome=Nome.from_str('Teste Nome')))], DataNasc=Datanasc.from_str('2023-01-01'), InfoNascimento=Infonascimento(Municipio=Municipio.from_str('Sao Paulo'), Bairro=Bairro.from_str('Centro'), PaisNasc=Paisnasc(Pais=Pais.from_str('BR'), AntigoNomePais=Antigonomepais.from_str('Teste Nome'))), EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), tpEndereco=Tpendereco.from_str('Rua Exemplo'), PaisEndereco=Paisendereco(Pais=Pais.from_str('BR')), EnderecoOutros=[Enderecooutros(tpEndereco=Tpendereco.from_str('Rua Exemplo'), EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), EnderecoEstrutura=Enderecoestrutura(EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), Endereco=Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345')), CEP=Cep.from_str('12345-678'), Municipio=Municipio.from_str('Sao Paulo'), UF=Uf.from_str('SP')), Pais=Pais.from_str('BR'))], paisResid=[Paisresid(Pais=Pais.from_str('BR'))], PaisNacionalidade=[Paisnacionalidade(Pais=Pais.from_str('BR'))], Proprietarios=[Proprietarios(tpNI=Tpni.from_str('1'), NIProprietario=Niproprietario.from_str('example'), tpProprietario=Tpproprietario.from_str('example'), NIF=[Nif(NumeroNIF=Numeronif.from_str('123'), PaisEmissaoNIF=Paisemissaonif.from_str('BR'), tpNIF=None)], Nome=Nome.from_str('Teste Nome'), tpNome=Tpnome.from_str('Teste Nome'), NomeOutros=[Nomeoutros(NomePF=Nomepf(tpNome=Tpnome.from_str('Teste Nome'), PrecTitulo=Prectitulo.from_str('example'), Titulo=[Titulo.from_str('example')], PrimeiroNome=Primeironome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), MeioNome=[Meionome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))], PrefixoNome=Prefixonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), UltimoNome=Ultimonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), IdGeracao=[Idgeracao.from_str('example')], Sufixo=[Sufixo.from_str('SP')], GenSufixo=Gensufixo.from_str('SP')), NomePJ=None)], EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), tpEndereco=Tpendereco.from_str('Rua Exemplo'), PaisEndereco=Paisendereco(Pais=Pais.from_str('BR')), EnderecoOutros=[Enderecooutros(tpEndereco=Tpendereco.from_str('Rua Exemplo'), EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), EnderecoEstrutura=Enderecoestrutura(EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), Endereco=Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345')), CEP=Cep.from_str('12345-678'), Municipio=Municipio.from_str('Sao Paulo'), UF=Uf.from_str('SP')), Pais=Pais.from_str('BR'))], paisResid=[Paisresid(Pais=Pais.from_str('BR'))], PaisNacionalidade=[Paisnacionalidade(Pais=Pais.from_str('BR'))], DataNasc=Datanasc.from_str('2023-01-01'), InfoNascimento=Infonascimento(Municipio=Municipio.from_str('Sao Paulo'), Bairro=Bairro.from_str('Centro'), PaisNasc=Paisnasc(Pais=Pais.from_str('BR'), AntigoNomePais=Antigonomepais.from_str('Teste Nome'))), Reportavel=[Reportavel(Pais=Pais.from_str('BR'))])])
        builder = IdedeclaradoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/ideDeclarado.xsd")


    def test_NIF(self):
        # Criar um objeto Nif de exemplo
        obj = Nif(NumeroNIF=Numeronif.from_str('123'), PaisEmissaoNIF=Paisemissaonif.from_str('BR'), tpNIF=Tpnif.from_str('1'))
        builder = NifXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/NIF.xsd")


    def test_NomeOutros(self):
        # Criar um objeto Nomeoutros de exemplo
        obj = Nomeoutros(NomePF=Nomepf(tpNome=Tpnome.from_str('Teste Nome'), PrecTitulo=Prectitulo.from_str('example'), Titulo=[Titulo.from_str('example')], PrimeiroNome=Primeironome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), MeioNome=[Meionome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))], PrefixoNome=Prefixonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), UltimoNome=Ultimonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), IdGeracao=[Idgeracao.from_str('example')], Sufixo=[Sufixo.from_str('SP')], GenSufixo=Gensufixo.from_str('SP')), NomePJ=Nomepj(tpNome=Tpnome.from_str('Teste Nome'), Nome=Nome.from_str('Teste Nome')))
        builder = NomeoutrosXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/NomeOutros.xsd")


    def test_NomePF(self):
        # Criar um objeto Nomepf de exemplo
        obj = Nomepf(tpNome=Tpnome.from_str('Teste Nome'), PrecTitulo=Prectitulo.from_str('example'), Titulo=[Titulo.from_str('example')], PrimeiroNome=Primeironome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), MeioNome=[Meionome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))], PrefixoNome=Prefixonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), UltimoNome=Ultimonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), IdGeracao=[Idgeracao.from_str('example')], Sufixo=[Sufixo.from_str('SP')], GenSufixo=Gensufixo.from_str('SP'))
        builder = NomepfXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/NomePF.xsd")


    def test_PrimeiroNome(self):
        # Criar um objeto Primeironome de exemplo
        obj = Primeironome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))
        builder = PrimeironomeXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/PrimeiroNome.xsd")


    def test_MeioNome(self):
        # Criar um objeto Meionome de exemplo
        obj = Meionome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))
        builder = MeionomeXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/MeioNome.xsd")


    def test_PrefixoNome(self):
        # Criar um objeto Prefixonome de exemplo
        obj = Prefixonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))
        builder = PrefixonomeXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/PrefixoNome.xsd")


    def test_UltimoNome(self):
        # Criar um objeto Ultimonome de exemplo
        obj = Ultimonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))
        builder = UltimonomeXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/UltimoNome.xsd")


    def test_NomePJ(self):
        # Criar um objeto Nomepj de exemplo
        obj = Nomepj(tpNome=Tpnome.from_str('Teste Nome'), Nome=Nome.from_str('Teste Nome'))
        builder = NomepjXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/NomePJ.xsd")


    def test_InfoNascimento(self):
        # Criar um objeto Infonascimento de exemplo
        obj = Infonascimento(Municipio=Municipio.from_str('Sao Paulo'), Bairro=Bairro.from_str('Centro'), PaisNasc=Paisnasc(Pais=Pais.from_str('BR'), AntigoNomePais=Antigonomepais.from_str('Teste Nome')))
        builder = InfonascimentoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/InfoNascimento.xsd")


    def test_PaisNasc(self):
        # Criar um objeto Paisnasc de exemplo
        obj = Paisnasc(Pais=Pais.from_str('BR'), AntigoNomePais=Antigonomepais.from_str('Teste Nome'))
        builder = PaisnascXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/PaisNasc.xsd")


    def test_PaisEndereco(self):
        # Criar um objeto Paisendereco de exemplo
        obj = Paisendereco(Pais=Pais.from_str('BR'))
        builder = PaisenderecoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/PaisEndereco.xsd")


    def test_EnderecoOutros(self):
        # Criar um objeto Enderecooutros de exemplo
        obj = Enderecooutros(tpEndereco=Tpendereco.from_str('Rua Exemplo'), EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), EnderecoEstrutura=Enderecoestrutura(EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), Endereco=Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345')), CEP=Cep.from_str('12345-678'), Municipio=Municipio.from_str('Sao Paulo'), UF=Uf.from_str('SP')), Pais=Pais.from_str('BR'))
        builder = EnderecooutrosXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/EnderecoOutros.xsd")


    def test_EnderecoEstrutura(self):
        # Criar um objeto Enderecoestrutura de exemplo
        obj = Enderecoestrutura(EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), Endereco=Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345')), CEP=Cep.from_str('12345-678'), Municipio=Municipio.from_str('Sao Paulo'), UF=Uf.from_str('SP'))
        builder = EnderecoestruturaXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/EnderecoEstrutura.xsd")


    def test_Endereco(self):
        # Criar um objeto Endereco de exemplo
        obj = Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345'))
        builder = EnderecoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/Endereco.xsd")


    def test_paisResid(self):
        # Criar um objeto Paisresid de exemplo
        obj = Paisresid(Pais=Pais.from_str('BR'))
        builder = PaisresidXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/paisResid.xsd")


    def test_PaisNacionalidade(self):
        # Criar um objeto Paisnacionalidade de exemplo
        obj = Paisnacionalidade(Pais=Pais.from_str('BR'))
        builder = PaisnacionalidadeXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/PaisNacionalidade.xsd")


    def test_Proprietarios(self):
        # Criar um objeto Proprietarios de exemplo
        obj = Proprietarios(tpNI=Tpni.from_str('1'), NIProprietario=Niproprietario.from_str('example'), tpProprietario=Tpproprietario.from_str('example'), NIF=[Nif(NumeroNIF=Numeronif.from_str('123'), PaisEmissaoNIF=Paisemissaonif.from_str('BR'), tpNIF=None)], Nome=Nome.from_str('Teste Nome'), tpNome=Tpnome.from_str('Teste Nome'), NomeOutros=[Nomeoutros(NomePF=Nomepf(tpNome=Tpnome.from_str('Teste Nome'), PrecTitulo=Prectitulo.from_str('example'), Titulo=[Titulo.from_str('example')], PrimeiroNome=Primeironome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), MeioNome=[Meionome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome'))], PrefixoNome=Prefixonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), UltimoNome=Ultimonome(Tipo=Tipo.from_str('example'), Nome=Nome.from_str('Teste Nome')), IdGeracao=[Idgeracao.from_str('example')], Sufixo=[Sufixo.from_str('SP')], GenSufixo=Gensufixo.from_str('SP')), NomePJ=None)], EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), tpEndereco=Tpendereco.from_str('Rua Exemplo'), PaisEndereco=Paisendereco(Pais=Pais.from_str('BR')), EnderecoOutros=[Enderecooutros(tpEndereco=Tpendereco.from_str('Rua Exemplo'), EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), EnderecoEstrutura=Enderecoestrutura(EnderecoLivre=Enderecolivre.from_str('Rua Exemplo'), Endereco=Endereco(Logradouro=Logradouro.from_str('Rua Exemplo'), Numero=Numero.from_str('123'), Complemento=Complemento.from_str('Apto 456'), Andar=Andar.from_str('5'), Bairro=Bairro.from_str('Centro'), CaixaPostal=Caixapostal.from_str('12345')), CEP=Cep.from_str('12345-678'), Municipio=Municipio.from_str('Sao Paulo'), UF=Uf.from_str('SP')), Pais=Pais.from_str('BR'))], paisResid=[Paisresid(Pais=Pais.from_str('BR'))], PaisNacionalidade=[Paisnacionalidade(Pais=Pais.from_str('BR'))], DataNasc=Datanasc.from_str('2023-01-01'), InfoNascimento=Infonascimento(Municipio=Municipio.from_str('Sao Paulo'), Bairro=Bairro.from_str('Centro'), PaisNasc=Paisnasc(Pais=Pais.from_str('BR'), AntigoNomePais=Antigonomepais.from_str('Teste Nome'))), Reportavel=[Reportavel(Pais=Pais.from_str('BR'))])
        builder = ProprietariosXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/Proprietarios.xsd")


    def test_Reportavel(self):
        # Criar um objeto Reportavel de exemplo
        obj = Reportavel(Pais=Pais.from_str('BR'))
        builder = ReportavelXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/Reportavel.xsd")


    def test_Caixa(self):
        # Criar um objeto Caixa de exemplo
        obj = Caixa(anoCaixa=Anocaixa.from_str('12345'), semestre=Semestre.from_str('1'), movOpFinAnual=Movopfinanual(Conta=[Conta(MedJudic=[Medjudic(NumProcJud=Numprocjud.from_str('example'), Vara=Vara.from_str('1'), SecJud=Secjud.from_str('1'), SubSecJud=Subsecjud.from_str('example'), dtConcessao=Dtconcessao.from_str('2023-01-01'), dtCassacao=Dtcassacao.from_str('2023-01-01'))], infoConta=Infoconta(Reportavel=[Reportavel(Pais=Pais.from_str('BR'))], tpConta=Tpconta.from_str('example'), subTpConta=Subtpconta.from_str('example'), tpNumConta=Tpnumconta.from_str('example'), numConta=Numconta.from_str('example'), tpRelacaoDeclarado=Tprelacaodeclarado.from_str('1'), moeda=Moeda.from_str('example'), Intermediario=Intermediario(GIIN=Giin.from_str('example'), tpNI=Tpni.from_str('1'), NIIntermediario=Niintermediario.from_str('example')), NoTitulares=Notitulares.from_str('example'), dtEncerramentoConta=Dtencerramentoconta.from_str('2023-01-01'), IndInatividade=Indinatividade.from_str('1'), IndNDoc=Indndoc.from_str('1'), Fundo=Fundo(GIIN=Giin.from_str('example'), CNPJ=Cnpj.from_str('12345678000195')), BalancoConta=Balancoconta(vlrUltDia=Vlrultdia.from_str('example')), PgtosAcum=[Pgtosacum(tpPgto=[Tppgto.from_str('example')], totPgtosAcum=Totpgtosacum.from_str('example'))]))]))
        builder = CaixaXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/Caixa.xsd")


    def test_movOpFinAnual(self):
        # Criar um objeto Movopfinanual de exemplo
        obj = Movopfinanual(Conta=[Conta(MedJudic=[Medjudic(NumProcJud=Numprocjud.from_str('example'), Vara=Vara.from_str('1'), SecJud=Secjud.from_str('1'), SubSecJud=Subsecjud.from_str('example'), dtConcessao=Dtconcessao.from_str('2023-01-01'), dtCassacao=Dtcassacao.from_str('2023-01-01'))], infoConta=Infoconta(Reportavel=[Reportavel(Pais=Pais.from_str('BR'))], tpConta=Tpconta.from_str('example'), subTpConta=Subtpconta.from_str('example'), tpNumConta=Tpnumconta.from_str('example'), numConta=Numconta.from_str('example'), tpRelacaoDeclarado=Tprelacaodeclarado.from_str('1'), moeda=Moeda.from_str('example'), Intermediario=Intermediario(GIIN=Giin.from_str('example'), tpNI=Tpni.from_str('1'), NIIntermediario=Niintermediario.from_str('example')), NoTitulares=Notitulares.from_str('example'), dtEncerramentoConta=Dtencerramentoconta.from_str('2023-01-01'), IndInatividade=Indinatividade.from_str('1'), IndNDoc=Indndoc.from_str('1'), Fundo=Fundo(GIIN=Giin.from_str('example'), CNPJ=Cnpj.from_str('12345678000195')), BalancoConta=Balancoconta(vlrUltDia=Vlrultdia.from_str('example')), PgtosAcum=[Pgtosacum(tpPgto=[Tppgto.from_str('example')], totPgtosAcum=Totpgtosacum.from_str('example'))]))])
        builder = MovopfinanualXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/movOpFinAnual.xsd")


    def test_Conta(self):
        # Criar um objeto Conta de exemplo
        obj = Conta(MedJudic=[Medjudic(NumProcJud=Numprocjud.from_str('example'), Vara=Vara.from_str('1'), SecJud=Secjud.from_str('1'), SubSecJud=Subsecjud.from_str('example'), dtConcessao=Dtconcessao.from_str('2023-01-01'), dtCassacao=Dtcassacao.from_str('2023-01-01'))], infoConta=Infoconta(Reportavel=[Reportavel(Pais=Pais.from_str('BR'))], tpConta=Tpconta.from_str('example'), subTpConta=Subtpconta.from_str('example'), tpNumConta=Tpnumconta.from_str('example'), numConta=Numconta.from_str('example'), tpRelacaoDeclarado=Tprelacaodeclarado.from_str('1'), moeda=Moeda.from_str('example'), Intermediario=Intermediario(GIIN=Giin.from_str('example'), tpNI=Tpni.from_str('1'), NIIntermediario=Niintermediario.from_str('example')), NoTitulares=Notitulares.from_str('example'), dtEncerramentoConta=Dtencerramentoconta.from_str('2023-01-01'), IndInatividade=Indinatividade.from_str('1'), IndNDoc=Indndoc.from_str('1'), Fundo=Fundo(GIIN=Giin.from_str('example'), CNPJ=Cnpj.from_str('12345678000195')), BalancoConta=Balancoconta(vlrUltDia=Vlrultdia.from_str('example')), PgtosAcum=[Pgtosacum(tpPgto=[Tppgto.from_str('example')], totPgtosAcum=Totpgtosacum.from_str('example'))]))
        builder = ContaXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/Conta.xsd")


    def test_MedJudic(self):
        # Criar um objeto Medjudic de exemplo
        obj = Medjudic(NumProcJud=Numprocjud.from_str('example'), Vara=Vara.from_str('1'), SecJud=Secjud.from_str('1'), SubSecJud=Subsecjud.from_str('example'), dtConcessao=Dtconcessao.from_str('2023-01-01'), dtCassacao=Dtcassacao.from_str('2023-01-01'))
        builder = MedjudicXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/MedJudic.xsd")


    def test_infoConta(self):
        # Criar um objeto Infoconta de exemplo
        obj = Infoconta(Reportavel=[Reportavel(Pais=Pais.from_str('BR'))], tpConta=Tpconta.from_str('example'), subTpConta=Subtpconta.from_str('example'), tpNumConta=Tpnumconta.from_str('example'), numConta=Numconta.from_str('example'), tpRelacaoDeclarado=Tprelacaodeclarado.from_str('1'), moeda=Moeda.from_str('example'), Intermediario=Intermediario(GIIN=Giin.from_str('example'), tpNI=Tpni.from_str('1'), NIIntermediario=Niintermediario.from_str('example')), NoTitulares=Notitulares.from_str('example'), dtEncerramentoConta=Dtencerramentoconta.from_str('2023-01-01'), IndInatividade=Indinatividade.from_str('1'), IndNDoc=Indndoc.from_str('1'), Fundo=Fundo(GIIN=Giin.from_str('example'), CNPJ=Cnpj.from_str('12345678000195')), BalancoConta=Balancoconta(vlrUltDia=Vlrultdia.from_str('example')), PgtosAcum=[Pgtosacum(tpPgto=[Tppgto.from_str('example')], totPgtosAcum=Totpgtosacum.from_str('example'))])
        builder = InfocontaXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/infoConta.xsd")


    def test_Intermediario(self):
        # Criar um objeto Intermediario de exemplo
        obj = Intermediario(GIIN=Giin.from_str('example'), tpNI=Tpni.from_str('1'), NIIntermediario=Niintermediario.from_str('example'))
        builder = IntermediarioXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/Intermediario.xsd")


    def test_Fundo(self):
        # Criar um objeto Fundo de exemplo
        obj = Fundo(GIIN=Giin.from_str('example'), CNPJ=Cnpj.from_str('12345678000195'))
        builder = FundoXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/Fundo.xsd")


    def test_BalancoConta(self):
        # Criar um objeto Balancoconta de exemplo
        obj = Balancoconta(vlrUltDia=Vlrultdia.from_str('example'))
        builder = BalancocontaXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/BalancoConta.xsd")


    def test_PgtosAcum(self):
        # Criar um objeto Pgtosacum de exemplo
        obj = Pgtosacum(tpPgto=[Tppgto.from_str('example')], totPgtosAcum=Totpgtosacum.from_str('example'))
        builder = PgtosacumXmlBuilder()
        self.validar_xml(obj, builder, "../schemas/subschemas/mov-op-fin-anual/PgtosAcum.xsd")

