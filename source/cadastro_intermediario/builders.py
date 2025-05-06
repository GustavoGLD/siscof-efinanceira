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


class EvtcadintermediarioXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Evtcadintermediario) -> ET.Element:
        el = XmlAdapter.create_element("evtCadIntermediario")
        el.set('id', str(obj.id))
        el.append(IdeeventoXmlBuilder().build(obj.ideEvento))
        el.append(IdedeclaranteXmlBuilder().build(obj.ideDeclarante))
        el.append(InfointermediarioXmlBuilder().build(obj.infoIntermediario))
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
        return el


class InfointermediarioXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Infointermediario) -> ET.Element:
        el = XmlAdapter.create_element("infoIntermediario")
        if obj.GIIN: XmlAdapter.append_child(el, 'GIIN', str(obj.GIIN))
        if obj.tpNI: XmlAdapter.append_child(el, 'tpNI', str(obj.tpNI))
        if obj.NIIntermediario: XmlAdapter.append_child(el, 'NIIntermediario', str(obj.NIIntermediario))
        XmlAdapter.append_child(el, 'nomeIntermediario', str(obj.nomeIntermediario))
        el.append(EnderecoXmlBuilder().build(obj.endereco))
        XmlAdapter.append_child(el, 'paisResidencia', str(obj.paisResidencia))
        return el


class EnderecoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Endereco) -> ET.Element:
        el = XmlAdapter.create_element("endereco")
        XmlAdapter.append_child(el, 'enderecoLivre', str(obj.enderecoLivre))
        XmlAdapter.append_child(el, 'municipio', str(obj.municipio))
        XmlAdapter.append_child(el, 'pais', str(obj.pais))
        return el
