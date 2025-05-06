import re
from typing import Optional, List, Literal


class Indretificacao:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Indretificacao":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Nrrecibo:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Nrrecibo":
        return cls(val)

    def __str__(self):
        return str(self.value)


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
    """CNPJ do Declarante"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Cnpjdeclarante":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Giin:
    """Global Intermediary Identification Number"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Giin":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Tpni:
    """Tipo de NI do intermediario"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Tpni":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Niintermediario:
    """Numero de identificacao do Intermediario"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Niintermediario":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Nomeintermediario:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Nomeintermediario":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Enderecolivre:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Enderecolivre":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Municipio:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Municipio":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Pais:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Pais":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Paisresidencia:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Paisresidencia":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Efinanceira:
    """"""
    def __init__(self, evtCadIntermediario: "Evtcadintermediario", Signature: "Signature"):
        self.evtCadIntermediario = evtCadIntermediario
        self.Signature = Signature


class Evtcadintermediario:
    """Evento de Cadastro do Intermediario"""
    def __init__(self, id: str, ideEvento: "Ideevento", ideDeclarante: "Idedeclarante", infoIntermediario: "Infointermediario"):
        self.id = id
        self.ideEvento = ideEvento
        self.ideDeclarante = ideDeclarante
        self.infoIntermediario = infoIntermediario


class Ideevento:
    """Informacoes de identificacao do evento"""
    def __init__(self, indRetificacao: "Indretificacao", nrRecibo: Optional["Nrrecibo"], tpAmb: "Tpamb", aplicEmi: "Aplicemi", verAplic: "Veraplic"):
        self.indRetificacao = indRetificacao
        self.nrRecibo = nrRecibo
        self.tpAmb = tpAmb
        self.aplicEmi = aplicEmi
        self.verAplic = verAplic


class Idedeclarante:
    """"""
    def __init__(self, cnpjDeclarante: "Cnpjdeclarante"):
        self.cnpjDeclarante = cnpjDeclarante


class Infointermediario:
    """"""
    def __init__(self, GIIN: Optional["Giin"], tpNI: Optional["Tpni"], NIIntermediario: Optional["Niintermediario"], nomeIntermediario: "Nomeintermediario", endereco: "Endereco", paisResidencia: "Paisresidencia"):
        self.GIIN = GIIN
        self.tpNI = tpNI
        self.NIIntermediario = NIIntermediario
        self.nomeIntermediario = nomeIntermediario
        self.endereco = endereco
        self.paisResidencia = paisResidencia


class Endereco:
    """"""
    def __init__(self, enderecoLivre: "Enderecolivre", municipio: "Municipio", pais: "Pais"):
        self.enderecoLivre = enderecoLivre
        self.municipio = municipio
        self.pais = pais


class Signature:
    """"""
    def __init__(self, SignedInfo: "Signedinfo", SignatureValue: "Signaturevalue", KeyInfo: Optional["Keyinfo"], Object: Optional[List["Object"]]):
        self.SignedInfo = SignedInfo
        self.SignatureValue = SignatureValue
        self.KeyInfo = KeyInfo
        self.Object = Object
