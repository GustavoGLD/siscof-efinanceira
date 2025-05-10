import xml.etree.ElementTree as ET
from .types import *
from typing import Dict, Optional
from abc import ABC, abstractmethod

class XmlBuilderInterface(ABC):
    @abstractmethod
    def build(self, obj) -> ET.Element: ...

class XmlAdapter:
    @staticmethod
    def create_element(tag: str, text: Optional[str]=None, attrib: Optional[Dict[str,str]]=None)->ET.Element:
        el=ET.Element(tag, attrib=attrib or {})
        if text is not None: el.text=text
        return el

    @staticmethod
    def append_child(parent: ET.Element, tag:str, text:Optional[str]=None, attrib:Optional[Dict[str,str]]=None)->ET.Element:
        ch=XmlAdapter.create_element(tag,text,attrib)
        parent.append(ch)
        return ch


class EvtmovopfinXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Evtmovopfin) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}evtMovOpFin")
        el.set('id', str(obj.id))
        el.append(IdeeventoXmlBuilder().build(obj.ideEvento))
        el.append(IdedeclaranteXmlBuilder().build(obj.ideDeclarante))
        el.append(IdedeclaradoXmlBuilder().build(obj.ideDeclarado))
        el.append(MescaixaXmlBuilder().build(obj.mesCaixa))
        return el


class IdeeventoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Ideevento) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}ideEvento")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}indRetificacao', str(obj.indRetificacao))
        if obj.nrRecibo: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}nrRecibo', str(obj.nrRecibo))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpAmb', str(obj.tpAmb))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}aplicEmi', str(obj.aplicEmi))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}verAplic', str(obj.verAplic))
        return el


class IdedeclaranteXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Idedeclarante) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}ideDeclarante")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}cnpjDeclarante', str(obj.cnpjDeclarante))
        return el


class IdedeclaradoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Idedeclarado) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}ideDeclarado")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpNI', str(obj.tpNI))
        if obj.tpDeclarado:
            for item in obj.tpDeclarado:
                XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpDeclarado', str(item))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NIDeclarado', str(obj.NIDeclarado))
        if obj.NIF:
            for item in obj.NIF:
                el.append(NifXmlBuilder().build(item))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NomeDeclarado', str(obj.NomeDeclarado))
        if obj.tpNomeDeclarado: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpNomeDeclarado', str(obj.tpNomeDeclarado))
        if obj.NomeOutros:
            for item in obj.NomeOutros:
                el.append(NomeoutrosXmlBuilder().build(item))
        if obj.DataNasc: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}DataNasc', str(obj.DataNasc))
        if obj.InfoNascimento: el.append(InfonascimentoXmlBuilder().build(obj.InfoNascimento))
        if obj.EnderecoLivre: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}EnderecoLivre', str(obj.EnderecoLivre))
        if obj.tpEndereco: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpEndereco', str(obj.tpEndereco))
        el.append(PaisenderecoXmlBuilder().build(obj.PaisEndereco))
        if obj.EnderecoOutros:
            for item in obj.EnderecoOutros:
                el.append(EnderecooutrosXmlBuilder().build(item))
        if obj.paisResid:
            for item in obj.paisResid:
                el.append(PaisresidXmlBuilder().build(item))
        if obj.PaisNacionalidade:
            for item in obj.PaisNacionalidade:
                el.append(PaisnacionalidadeXmlBuilder().build(item))
        if obj.Proprietarios:
            for item in obj.Proprietarios:
                el.append(ProprietariosXmlBuilder().build(item))
        return el


class NifXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Nif) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NIF")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NumeroNIF', str(obj.NumeroNIF))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}PaisEmissaoNIF', str(obj.PaisEmissaoNIF))
        if obj.tpNIF: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpNIF', str(obj.tpNIF))
        return el


class NomeoutrosXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Nomeoutros) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NomeOutros")
        if obj.NomePF: el.append(NomepfXmlBuilder().build(obj.NomePF))
        if obj.NomePJ: el.append(NomepjXmlBuilder().build(obj.NomePJ))
        return el


class NomepfXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Nomepf) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NomePF")
        if obj.tpNome: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpNome', str(obj.tpNome))
        if obj.PrecTitulo: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}PrecTitulo', str(obj.PrecTitulo))
        if obj.Titulo:
            for item in obj.Titulo:
                XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Titulo', str(item))
        el.append(PrimeironomeXmlBuilder().build(obj.PrimeiroNome))
        if obj.MeioNome:
            for item in obj.MeioNome:
                el.append(MeionomeXmlBuilder().build(item))
        if obj.PrefixoNome: el.append(PrefixonomeXmlBuilder().build(obj.PrefixoNome))
        el.append(UltimonomeXmlBuilder().build(obj.UltimoNome))
        if obj.IdGeracao:
            for item in obj.IdGeracao:
                XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}IdGeracao', str(item))
        if obj.Sufixo:
            for item in obj.Sufixo:
                XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Sufixo', str(item))
        if obj.GenSufixo: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}GenSufixo', str(obj.GenSufixo))
        return el


class PrimeironomeXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Primeironome) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}PrimeiroNome")
        if obj.Tipo: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Tipo', str(obj.Tipo))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Nome', str(obj.Nome))
        return el


class MeionomeXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Meionome) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}MeioNome")
        if obj.Tipo: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Tipo', str(obj.Tipo))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Nome', str(obj.Nome))
        return el


class PrefixonomeXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Prefixonome) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}PrefixoNome")
        if obj.Tipo: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Tipo', str(obj.Tipo))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Nome', str(obj.Nome))
        return el


class UltimonomeXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Ultimonome) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}UltimoNome")
        if obj.Tipo: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Tipo', str(obj.Tipo))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Nome', str(obj.Nome))
        return el


class NomepjXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Nomepj) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NomePJ")
        if obj.tpNome: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpNome', str(obj.tpNome))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Nome', str(obj.Nome))
        return el


class InfonascimentoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Infonascimento) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}InfoNascimento")
        if obj.Municipio: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Municipio', str(obj.Municipio))
        if obj.Bairro: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Bairro', str(obj.Bairro))
        if obj.PaisNasc: el.append(PaisnascXmlBuilder().build(obj.PaisNasc))
        return el


class PaisnascXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Paisnasc) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}PaisNasc")
        if obj.Pais: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Pais', str(obj.Pais))
        if obj.AntigoNomePais: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}AntigoNomePais', str(obj.AntigoNomePais))
        return el


class PaisenderecoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Paisendereco) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}PaisEndereco")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Pais', str(obj.Pais))
        return el


class EnderecooutrosXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Enderecooutros) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}EnderecoOutros")
        if obj.tpEndereco: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpEndereco', str(obj.tpEndereco))
        if obj.EnderecoLivre: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}EnderecoLivre', str(obj.EnderecoLivre))
        if obj.EnderecoEstrutura: el.append(EnderecoestruturaXmlBuilder().build(obj.EnderecoEstrutura))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Pais', str(obj.Pais))
        return el


class EnderecoestruturaXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Enderecoestrutura) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}EnderecoEstrutura")
        if obj.EnderecoLivre: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}EnderecoLivre', str(obj.EnderecoLivre))
        if obj.Endereco: el.append(EnderecoXmlBuilder().build(obj.Endereco))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}CEP', str(obj.CEP))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Municipio', str(obj.Municipio))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}UF', str(obj.UF))
        return el


class EnderecoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Endereco) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Endereco")
        if obj.Logradouro: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Logradouro', str(obj.Logradouro))
        if obj.Numero: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Numero', str(obj.Numero))
        if obj.Complemento: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Complemento', str(obj.Complemento))
        if obj.Andar: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Andar', str(obj.Andar))
        if obj.Bairro: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Bairro', str(obj.Bairro))
        if obj.CaixaPostal: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}CaixaPostal', str(obj.CaixaPostal))
        return el


class PaisresidXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Paisresid) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}paisResid")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Pais', str(obj.Pais))
        return el


class PaisnacionalidadeXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Paisnacionalidade) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}PaisNacionalidade")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Pais', str(obj.Pais))
        return el


class ProprietariosXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Proprietarios) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Proprietarios")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpNI', str(obj.tpNI))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NIProprietario', str(obj.NIProprietario))
        if obj.tpProprietario: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpProprietario', str(obj.tpProprietario))
        if obj.NIF:
            for item in obj.NIF:
                el.append(NifXmlBuilder().build(item))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Nome', str(obj.Nome))
        if obj.tpNome: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpNome', str(obj.tpNome))
        if obj.NomeOutros:
            for item in obj.NomeOutros:
                el.append(NomeoutrosXmlBuilder().build(item))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}EnderecoLivre', str(obj.EnderecoLivre))
        if obj.tpEndereco: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpEndereco', str(obj.tpEndereco))
        el.append(PaisenderecoXmlBuilder().build(obj.PaisEndereco))
        if obj.EnderecoOutros:
            for item in obj.EnderecoOutros:
                el.append(EnderecooutrosXmlBuilder().build(item))
        if obj.paisResid:
            for item in obj.paisResid:
                el.append(PaisresidXmlBuilder().build(item))
        if obj.PaisNacionalidade:
            for item in obj.PaisNacionalidade:
                el.append(PaisnacionalidadeXmlBuilder().build(item))
        if obj.DataNasc: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}DataNasc', str(obj.DataNasc))
        if obj.InfoNascimento: el.append(InfonascimentoXmlBuilder().build(obj.InfoNascimento))
        if obj.Reportavel:
            for item in obj.Reportavel:
                el.append(ReportavelXmlBuilder().build(item))
        return el


class ReportavelXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Reportavel) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Reportavel")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Pais', str(obj.Pais))
        return el


class MescaixaXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Mescaixa) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}mesCaixa")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}anoMesCaixa', str(obj.anoMesCaixa))
        el.append(MovopfinXmlBuilder().build(obj.movOpFin))
        return el


class MovopfinXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Movopfin) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}movOpFin")
        if obj.Conta:
            for item in obj.Conta:
                el.append(ContaXmlBuilder().build(item))
        if obj.Cambio: el.append(CambioXmlBuilder().build(obj.Cambio))
        return el


class ContaXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Conta) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Conta")
        if obj.MedJudic:
            for item in obj.MedJudic:
                el.append(MedjudicXmlBuilder().build(item))
        if obj.infoConta: el.append(InfocontaXmlBuilder().build(obj.infoConta))
        return el


class MedjudicXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Medjudic) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}MedJudic")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NumProcJud', str(obj.NumProcJud))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Vara', str(obj.Vara))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}SecJud', str(obj.SecJud))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}SubSecJud', str(obj.SubSecJud))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}dtConcessao', str(obj.dtConcessao))
        if obj.dtCassacao: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}dtCassacao', str(obj.dtCassacao))
        return el


class InfocontaXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Infoconta) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}infoConta")
        if obj.Reportavel:
            for item in obj.Reportavel:
                el.append(ReportavelXmlBuilder().build(item))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpConta', str(obj.tpConta))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}subTpConta', str(obj.subTpConta))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpNumConta', str(obj.tpNumConta))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}numConta', str(obj.numConta))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpRelacaoDeclarado', str(obj.tpRelacaoDeclarado))
        if obj.moeda: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}moeda', str(obj.moeda))
        if obj.Intermediario: el.append(IntermediarioXmlBuilder().build(obj.Intermediario))
        if obj.NoTitulares: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NoTitulares', str(obj.NoTitulares))
        if obj.dtEncerramentoConta: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}dtEncerramentoConta', str(obj.dtEncerramentoConta))
        if obj.IndInatividade: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}IndInatividade', str(obj.IndInatividade))
        if obj.IndNDoc: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}IndNDoc', str(obj.IndNDoc))
        if obj.Fundo: el.append(FundoXmlBuilder().build(obj.Fundo))
        el.append(BalancocontaXmlBuilder().build(obj.BalancoConta))
        if obj.PgtosAcum:
            for item in obj.PgtosAcum:
                el.append(PgtosacumXmlBuilder().build(item))
        return el


class IntermediarioXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Intermediario) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Intermediario")
        if obj.GIIN: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}GIIN', str(obj.GIIN))
        if obj.tpNI: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpNI', str(obj.tpNI))
        if obj.NIIntermediario: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}NIIntermediario', str(obj.NIIntermediario))
        return el


class FundoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Fundo) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Fundo")
        if obj.GIIN: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}GIIN', str(obj.GIIN))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}CNPJ', str(obj.CNPJ))
        return el


class BalancocontaXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Balancoconta) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}BalancoConta")
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}totCreditos', str(obj.totCreditos))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}totDebitos', str(obj.totDebitos))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}totCreditosMesmaTitularidade', str(obj.totCreditosMesmaTitularidade))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}totDebitosMesmaTitularidade', str(obj.totDebitosMesmaTitularidade))
        if obj.vlrUltDia: XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}vlrUltDia', str(obj.vlrUltDia))
        return el


class PgtosacumXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Pgtosacum) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}PgtosAcum")
        if obj.tpPgto:
            for item in obj.tpPgto:
                XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}tpPgto', str(item))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}totPgtosAcum', str(obj.totPgtosAcum))
        return el


class CambioXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Cambio) -> ET.Element:
        el = XmlAdapter.create_element("{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}Cambio")
        if obj.MedJudic:
            for item in obj.MedJudic:
                el.append(MedjudicXmlBuilder().build(item))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}totCompras', str(obj.totCompras))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}totVendas', str(obj.totVendas))
        XmlAdapter.append_child(el, '{http://www.eFinanceira.gov.br/schemas/evtMovOpFin/v1_2_1}totTransferencias', str(obj.totTransferencias))
        return el
