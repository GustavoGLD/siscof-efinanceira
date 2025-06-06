import re
from typing import Optional, List, Literal


class Tpamb:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Tpamb":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Aplicemi:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Aplicemi":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Veraplic:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Veraplic":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Cnpjdeclarante:
    """CNPJ da Entidade Declarante"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Cnpjdeclarante":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Nrreciboevento:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Nrreciboevento":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Efinanceira:
    """"""
    def __init__(self, evtExclusao: "Evtexclusao", Signature: "Signature"):
        self.evtExclusao = evtExclusao
        self.Signature = Signature


class Evtexclusao:
    """
    ATENÇÃO!!! ESTE EVENTO SÓ DEVE SER UTILIZADO SE HOUVER A
    INTENÇÃO DE EXCLUIR TODA UMA E-FINANCEIRA “EM ANDAMENTO” DE
    DETERMINADO PERÍODO!!! TODA A E-FINANCEIRA E SEUS RESPECTIVOS
    EVENTOS DE MOVIMENTO SERÃO EXCLUÍDOS!!! PARA A EXCLUSÃO
    PONTUAL, DE DETERMINADOS EVENTOS INDIVIDUALMENTE, UTILIZE O
    EVENTO DE EXCLUSÃO, DESCRITO NO ITEM 3.4 DESTE MANUAL!!!
    """
    def __init__(self, id: str, ideEvento: "Ideevento", ideDeclarante: "Idedeclarante", infoExclusao: "Infoexclusao"):
        self.id = id
        self.ideEvento = ideEvento
        self.ideDeclarante = ideDeclarante
        self.infoExclusao = infoExclusao


class Ideevento:
    """Informacoes de identificacao do evento"""
    def __init__(self, tpAmb: "Tpamb", aplicEmi: "Aplicemi", verAplic: "Veraplic"):
        self.tpAmb = tpAmb
        self.aplicEmi = aplicEmi
        self.verAplic = verAplic


class Idedeclarante:
    """"""
    def __init__(self, cnpjDeclarante: "Cnpjdeclarante"):
        self.cnpjDeclarante = cnpjDeclarante


class Infoexclusao:
    """"""
    def __init__(self, nrReciboEvento: "Nrreciboevento"):
        self.nrReciboEvento = nrReciboEvento


class Signature:
    """"""
    def __init__(self, SignedInfo: "Signedinfo", SignatureValue: "Signaturevalue", KeyInfo: Optional["Keyinfo"], Object: Optional[List["Object"]]):
        self.SignedInfo = SignedInfo
        self.SignatureValue = SignatureValue
        self.KeyInfo = KeyInfo
        self.Object = Object
