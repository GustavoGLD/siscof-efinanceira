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


class EvtcadpatrocinadoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Evtcadpatrocinado) -> ET.Element:
        el = XmlAdapter.create_element("evtCadPatrocinado")
        el.set('id', str(obj.id))
        el.append(IdeeventoXmlBuilder().build(obj.ideEvento))
        el.append(IdedeclaranteXmlBuilder().build(obj.ideDeclarante))
        el.append(InfopatrocinadoXmlBuilder().build(obj.infoPatrocinado))
        return el


class IdeeventoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Ideevento) -> ET.Element:
        el = XmlAdapter.create_element("ideEvento")
        XmlAdapter.append_child(el, 'indRetificacao', str(obj.indRetificacao))
        if obj.nrRecibo: XmlAdapter.append_child(el, 'nrRecibo', str(obj.nrRecibo))
        XmlAdapter.append_child(el, 'tpAmb', str(obj.tpAmb))
        XmlAdapter.append_child(el, 'aplicEmi', str(obj.aplicEmi))
        XmlAdapter.append_child(el, 'verAplic', str(obj.verAplic))
        return el


class IdedeclaranteXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Idedeclarante) -> ET.Element:
        el = XmlAdapter.create_element("ideDeclarante")
        XmlAdapter.append_child(el, 'cnpjDeclarante', str(obj.cnpjDeclarante))
        if obj.GIIN: XmlAdapter.append_child(el, 'GIIN', str(obj.GIIN))
        if obj.CategoriaPatrocinador: XmlAdapter.append_child(el, 'CategoriaPatrocinador', str(obj.CategoriaPatrocinador))
        return el


class InfopatrocinadoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Infopatrocinado) -> ET.Element:
        el = XmlAdapter.create_element("infoPatrocinado")
        if obj.GIIN: XmlAdapter.append_child(el, 'GIIN', str(obj.GIIN))
        XmlAdapter.append_child(el, 'CNPJ', str(obj.CNPJ))
        if obj.NIF:
            for item in obj.NIF:
                el.append(NifXmlBuilder().build(item))
        XmlAdapter.append_child(el, 'nomePatrocinado', str(obj.nomePatrocinado))
        if obj.tpNome: XmlAdapter.append_child(el, 'tpNome', str(obj.tpNome))
        el.append(EnderecoEntidadePatrocinadaXmlBuilder().build(obj.endereco))
        if obj.tpEndereco: XmlAdapter.append_child(el, 'tpEndereco', str(obj.tpEndereco))
        if obj.EnderecoOutros:
            for item in obj.EnderecoOutros:
                el.append(EnderecooutrosXmlBuilder().build(item))
        if obj.paisResid:
            for item in obj.paisResid:
                el.append(PaisresidXmlBuilder().build(item))
        return el


class NifXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Nif) -> ET.Element:
        el = XmlAdapter.create_element("NIF")
        XmlAdapter.append_child(el, 'NumeroNIF', str(obj.NumeroNIF))
        XmlAdapter.append_child(el, 'PaisEmissao', str(obj.PaisEmissao))
        if obj.tpNIF: XmlAdapter.append_child(el, 'tpNIF', str(obj.tpNIF))
        return el


class EnderecoEntidadePatrocinadaXmlBuilder(XmlBuilderInterface):
    def build(self, obj: EnderecoEntidadePatrocinada) -> ET.Element:
        el = XmlAdapter.create_element("endereco")
        XmlAdapter.append_child(el, 'enderecoLivre', str(obj.enderecoLivre))
        XmlAdapter.append_child(el, 'CEP', str(obj.CEP))
        XmlAdapter.append_child(el, 'municipio', str(obj.municipio))
        XmlAdapter.append_child(el, 'pais', str(obj.pais))
        return el


class EnderecooutrosXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Enderecooutros) -> ET.Element:
        el = XmlAdapter.create_element("EnderecoOutros")
        if obj.tpEndereco: XmlAdapter.append_child(el, 'tpEndereco', str(obj.tpEndereco))
        if obj.EnderecoLivre: XmlAdapter.append_child(el, 'EnderecoLivre', str(obj.EnderecoLivre))
        if obj.EnderecoEstrutura: el.append(EnderecoestruturaXmlBuilder().build(obj.EnderecoEstrutura))
        XmlAdapter.append_child(el, 'Pais', str(obj.Pais))
        return el


class EnderecoestruturaXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Enderecoestrutura) -> ET.Element:
        el = XmlAdapter.create_element("EnderecoEstrutura")
        if obj.EnderecoLivre: XmlAdapter.append_child(el, 'EnderecoLivre', str(obj.EnderecoLivre))
        if obj.Endereco: el.append(EnderecoXmlBuilder().build(obj.Endereco))
        XmlAdapter.append_child(el, 'CEP', str(obj.CEP))
        XmlAdapter.append_child(el, 'Municipio', str(obj.Municipio))
        XmlAdapter.append_child(el, 'UF', str(obj.UF))
        return el


class EnderecoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Endereco) -> ET.Element:
        el = XmlAdapter.create_element("Endereco")
        if obj.Logradouro: XmlAdapter.append_child(el, 'Logradouro', str(obj.Logradouro))
        if obj.Numero: XmlAdapter.append_child(el, 'Numero', str(obj.Numero))
        if obj.Complemento: XmlAdapter.append_child(el, 'Complemento', str(obj.Complemento))
        if obj.Andar: XmlAdapter.append_child(el, 'Andar', str(obj.Andar))
        if obj.Bairro: XmlAdapter.append_child(el, 'Bairro', str(obj.Bairro))
        if obj.CaixaPostal: XmlAdapter.append_child(el, 'CaixaPostal', str(obj.CaixaPostal))
        return el


class PaisresidXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Paisresid) -> ET.Element:
        el = XmlAdapter.create_element("paisResid")
        XmlAdapter.append_child(el, 'Pais', str(obj.Pais))
        return el

