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
    """CNPJ da Entidade Declarante"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Cnpjdeclarante":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Giin:
    """GIIN (Global Intermediary Identification Number) de Patrocinador (formato: XXXXXX.XXXXX.SP.XXX)"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Giin":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Categoriapatrocinador:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Categoriapatrocinador":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Cnpj:
    """CNPJ da Entidade Patrocinada"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Cnpj":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Numeronif:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Numeronif":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Paisemissao:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Paisemissao":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Tpnif:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Tpnif":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Nomepatrocinado:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Nomepatrocinado":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Tpnome:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Tpnome":
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


class Cep:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Cep":
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


class Tpendereco:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Tpendereco":
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


class Logradouro:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Logradouro":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Numero:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Numero":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Complemento:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Complemento":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Andar:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Andar":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Bairro:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Bairro":
        return cls(val)

    def __str__(self):
        return str(self.value)


class Caixapostal:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Caixapostal":
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


class Uf:
    """"""
    def __init__(self, value: str):
        pass
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Uf":
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


class Efinanceira:
    """"""
    def __init__(self, evtCadPatrocinado: "Evtcadpatrocinado", Signature: "Signature"):
        self.evtCadPatrocinado = evtCadPatrocinado
        self.Signature = Signature


class Evtcadpatrocinado:
    """Evento de Cadastro do Patrocinado"""
    def __init__(self, id: str, ideEvento: "Ideevento", ideDeclarante: "Idedeclarante", infoPatrocinado: "Infopatrocinado"):
        self.id = id
        self.ideEvento = ideEvento
        self.ideDeclarante = ideDeclarante
        self.infoPatrocinado = infoPatrocinado


class Ideevento:
    """Informacoes de identificacao do evento"""
    def __init__(self, indRetificacao: "Indretificacao", nrRecibo: Optional["Nrrecibo"], tpAmb: "Tpamb", aplicEmi: "Aplicemi", verAplic: "Veraplic"):
        self.indRetificacao = indRetificacao
        self.nrRecibo = nrRecibo
        self.tpAmb = tpAmb
        self.aplicEmi = aplicEmi
        self.verAplic = verAplic


class Idedeclarante:
    """Informacoes de identificacao da Entidade Declarante"""
    def __init__(self, cnpjDeclarante: "Cnpjdeclarante", GIIN: Optional["Giin"], CategoriaPatrocinador: Optional["Categoriapatrocinador"]):
        self.cnpjDeclarante = cnpjDeclarante
        self.GIIN = GIIN
        self.CategoriaPatrocinador = CategoriaPatrocinador


class Infopatrocinado:
    """Informacoes da Entidade Patrocinada"""
    def __init__(self, GIIN: Optional["Giin"], CNPJ: "Cnpj", NIF: Optional[List["Nif"]], nomePatrocinado: "Nomepatrocinado", tpNome: Optional["Tpnome"], endereco: "EnderecoEntidadePatrocinada", tpEndereco: Optional["Tpendereco"], EnderecoOutros: Optional[List["Enderecooutros"]], paisResid: List["Paisresid"]):
        self.GIIN = GIIN
        self.CNPJ = CNPJ
        self.NIF = NIF
        self.nomePatrocinado = nomePatrocinado
        self.tpNome = tpNome
        self.endereco = endereco
        self.tpEndereco = tpEndereco
        self.EnderecoOutros = EnderecoOutros
        self.paisResid = paisResid


class Nif:
    """Informacoes de Identificacao Fiscal no Exterior da Entidade Patrocinada"""
    def __init__(self, NumeroNIF: "Numeronif", PaisEmissao: "Paisemissao", tpNIF: Optional["Tpnif"]):
        self.NumeroNIF = NumeroNIF
        self.PaisEmissao = PaisEmissao
        self.tpNIF = tpNIF


class EnderecoEntidadePatrocinada:
    """Endereco da Entidade Patrocinada"""
    def __init__(self, enderecoLivre: "Enderecolivre", CEP: "Cep", municipio: "Municipio", pais: "Pais"):
        self.enderecoLivre = enderecoLivre
        self.CEP = CEP
        self.municipio = municipio
        self.pais = pais


class Enderecooutros:
    """Demais enderecos"""
    def __init__(self, tpEndereco: Optional["Tpendereco"], EnderecoLivre: Optional["Enderecolivre"], EnderecoEstrutura: Optional["Enderecoestrutura"], Pais: "Pais"):
        self.tpEndereco = tpEndereco
        self.EnderecoLivre = EnderecoLivre
        self.EnderecoEstrutura = EnderecoEstrutura
        self.Pais = Pais


class Enderecoestrutura:
    """Endereco na forma estruturada"""
    def __init__(self, EnderecoLivre: Optional["Enderecolivre"], Endereco: Optional["Endereco"], CEP: "Cep", Municipio: "Municipio", UF: "Uf"):
        self.EnderecoLivre = EnderecoLivre
        self.Endereco = Endereco
        self.CEP = CEP
        self.Municipio = Municipio
        self.UF = UF


class Endereco:
    """Dados do endereco na forma estruturada"""
    def __init__(self, Logradouro: Optional["Logradouro"], Numero: Optional["Numero"], Complemento: Optional["Complemento"], Andar: Optional["Andar"], Bairro: Optional["Bairro"], CaixaPostal: Optional["Caixapostal"]):
        self.Logradouro = Logradouro
        self.Numero = Numero
        self.Complemento = Complemento
        self.Andar = Andar
        self.Bairro = Bairro
        self.CaixaPostal = CaixaPostal


class Paisresid:
    """Pais de residencia da Entidade Patrocinada"""
    def __init__(self, Pais: "Pais"):
        self.Pais = Pais


class Signature:
    """"""
    def __init__(self, SignedInfo: "Signedinfo", SignatureValue: "Signaturevalue", KeyInfo: Optional["Keyinfo"], Object: Optional[List["Object"]]):
        self.SignedInfo = SignedInfo
        self.SignatureValue = SignatureValue
        self.KeyInfo = KeyInfo
        self.Object = Object
