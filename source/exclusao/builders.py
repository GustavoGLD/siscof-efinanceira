import xml.etree.ElementTree as ET
from source.exclusao.types import *
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


class EvtexclusaoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Evtexclusao) -> ET.Element:
        el = XmlAdapter.create_element("evtExclusao")
        el.set('id', str(obj.id))
        el.append(IdeeventoXmlBuilder().build(obj.ideEvento))
        el.append(IdedeclaranteXmlBuilder().build(obj.ideDeclarante))
        el.append(InfoexclusaoXmlBuilder().build(obj.infoExclusao))
        return el


class IdeeventoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Ideevento) -> ET.Element:
        el = XmlAdapter.create_element("ideEvento")
        XmlAdapter.append_child(el, 'tpAmb', str(obj.tpAmb))
        XmlAdapter.append_child(el, 'aplicEmi', str(obj.aplicEmi))
        XmlAdapter.append_child(el, 'verAplic', str(obj.verAplic))
        return el


class IdedeclaranteXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Idedeclarante) -> ET.Element:
        el = XmlAdapter.create_element("ideDeclarante")
        XmlAdapter.append_child(el, 'cnpjDeclarante', str(obj.cnpjDeclarante))
        return el


class InfoexclusaoXmlBuilder(XmlBuilderInterface):
    def build(self, obj: Infoexclusao) -> ET.Element:
        el = XmlAdapter.create_element("infoExclusao")
        XmlAdapter.append_child(el, 'nrReciboEvento', str(obj.nrReciboEvento))
        return el
