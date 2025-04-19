"""
Módulo gerado a partir da estrutura UML do eFinanceira.
Contém as classes de Value Objects e Entidades com suas validações e
docstrings conforme a documentação original.
"""

import re
from typing import Optional, List

# =============================================================================
#                               VALUE OBJECTS
# =============================================================================

class ID:
    """ID – minLength: 13, maxLength: 20"""
    def __init__(self, value: str):
        if not value or not (13 <= len(value) <= 20):
            raise ValueError("ID inválido: tamanho deve estar entre 13 e 20 caracteres")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "ID":
        return cls(val)

    def __str__(self):
        return self.value


class IndRetificacao:
    """Indicativo de Retificação:
    1 - Original
    2 - Retificador
    3 - Retificador a Pedido"""
    def __init__(self, value: str):
        if value not in ["1", "2", "3"]:
            raise ValueError("Indicativo de retificação inválido")
        self.value = value

    @classmethod
    def identificar_como_original(cls) -> "IndRetificacao":
        return cls("1")

    @classmethod
    def identificar_como_retificador(cls) -> "IndRetificacao":
        return cls("2")

    @classmethod
    def identificar_como_retificador_pedido(cls) -> "IndRetificacao":
        return cls("3")

    def __str__(self):
        return self.value


class NumeroRecibo:
    """Número do recibo do arquivo a ser retificado"""
    def __init__(self, value: str):
        padrao = r'^[0-9]{1,18}-[0-9]{2}-[0-9]{3}-[0-9]{4}-[0-9]{1,18}$'
        if not value or not (15 <= len(value) <= 49):
            raise ValueError("Número do recibo inválido: tamanho deve estar entre 15 e 49 caracteres")
        if not re.fullmatch(padrao, value):
            raise ValueError("Número do recibo inválido\nFormato esperado: \"[0-9]{1,18}-[0-9]{2}-[0-9]{3}-[0-9]{4}-[0-9]{1,18}\"")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "NumeroRecibo":
        return cls(val)

    def __str__(self):
        return self.value


class TpAmb:
    """Identificação do ambiente:
    1 - Produção
    2 - Homologação"""
    def __init__(self, value: str):
        if value not in ["1", "2"]:
            raise ValueError("Ambiente (tpAmb) inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "TpAmb":
        return cls(val)

    def __str__(self):
        return self.value


class AplicEmi:
    """Processo de emissão do evento:
    1- Emissão com aplicativo da empresa"""
    def __init__(self, value: str):
        # Apesar de o padrão estar definido como "[1|2]", a documentação apresenta somente a opção 1.
        if value not in ["1", "2"]:
            raise ValueError("Aplicação de emissão (aplicEmi) inválida")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "AplicEmi":
        return cls(val)

    def __str__(self):
        return self.value


class VerAplic:
    """Versão do aplicativo de emissão do evento"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 20):
            raise ValueError("Versão do aplicativo (verAplic) inválida")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "VerAplic":
        return cls(val)

    def __str__(self):
        return self.value


class CnpjDeclarante:
    """CNPJ da Entidade Declarante"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 14):
            raise ValueError("CNPJ da Entidade Declarante inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "CnpjDeclarante":
        return cls(val)

    def __str__(self):
        return self.value


class GIIN:
    """Global Intermediary Identification Number"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 19):
            raise ValueError("GIIN inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "GIIN":
        return cls(val)

    def __str__(self):
        return self.value


class CategoriaDeclarante:
    """Tipo da categoria"""
    def __init__(self, value: str):
        if value is None:
            value = ""
        if len(value) > 8:
            raise ValueError("CategoriaDeclarante inválida: tamanho máximo é 8")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "CategoriaDeclarante":
        return cls(val)

    def __str__(self):
        return self.value


class TpInstPgto:
    """
    1 - Emissor de Instrumento de Pagamento Pos- Pago: Entidade que gerencia contas de pagamento do tipo pós-pagas, na qual os recursos são depositados pelo declarado para pagamento de débitos já assumidos.
    2 - Credenciador: Instituição de pagamento que credencia a aceitação de instrumento de pagamento.
    3 - Sub-credenciador: O participante do arranjo de pagamento que habilita usuário final recebedor para a aceitação de instrumento de pagamento
    """

    def __init__(self, value: str):
        if value not in ["1", "2", "3"]:
            raise ValueError("Tipo de Instituição de Pagamento (tpInstPgto) inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "TpInstPgto":
        return cls(val)

    def __str__(self):
        return self.value


class NumeroNIF:
    """Número de Identificação Fiscal no Exterior"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 25):
            raise ValueError("Número NIF inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "NumeroNIF":
        return cls(val)

    def __str__(self):
        return self.value


class PaisEmissao:
    """Pais de emissão do NIF"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 2):
            raise ValueError("País de emissão inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "PaisEmissao":
        return cls(val)

    def __str__(self):
        return self.value


class TpNIF:
    """Tipo do NIF"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 30):
            raise ValueError("Tipo do NIF inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "TpNIF":
        return cls(val)

    def __str__(self):
        return self.value


class Nome:
    """Nome da Entidade Declarante"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 100):
            raise ValueError("Nome inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Nome":
        return cls(val)

    def __str__(self):
        return self.value


class TpNome:
    """Tipo do nome da Entidade Declarante"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 7):
            raise ValueError("Tipo do nome inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "TpNome":
        return cls(val)

    def __str__(self):
        return self.value


class EnderecoLivre:
    """Endereço principal da Entidade Declarante"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 200):
            raise ValueError("Endereço livre inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "EnderecoLivre":
        return cls(val)

    def __str__(self):
        return self.value


class TpEndereco:
    """Tipo do endereço principal da Entidade Declarante"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 7):
            raise ValueError("Tipo de endereço inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "TpEndereco":
        return cls(val)

    def __str__(self):
        return self.value


class Municipio:
    """Código do município da Entidade Declarante"""
    def __init__(self, value: int):
        # Verifica se o número possui no máximo 7 dígitos
        if not isinstance(value, int) or len(str(value)) > 7:
            raise ValueError("Município inválido: deve ser um inteiro com até 7 dígitos")
        self.value = value

    @classmethod
    def from_int(cls, val: int) -> "Municipio":
        return cls(val)

    def __str__(self):
        return str(self.value)


class UF:
    """Sigla da Unidade da Federação da Entidade Declarante"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 2):
            raise ValueError("UF inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "UF":
        return cls(val)

    def __str__(self):
        return self.value


class CEP:
    """Código de Endereçamento Postal da Entidade Declarante"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 8):
            raise ValueError("CEP inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "CEP":
        return cls(val)

    def __str__(self):
        return self.value


class Pais:
    """País do endereço da Entidade Declarante"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 2):
            raise ValueError("País inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Pais":
        return cls(val)

    def __str__(self):
        return self.value


class PaisResidPais:
    """Sigla do país de residência da Entidade Declarante"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 2):
            raise ValueError("País de residência inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "PaisResidPais":
        return cls(val)

    def __str__(self):
        return self.value


class EnderecoOutrosTpEndereco:
    """Tipo do endereço"""
    def __init__(self, value: str):
        # minOccurs: 0, maxLength: 7; caso seja informado, valida
        if value is not None and not (1 <= len(value) <= 7):
            raise ValueError("Tipo do endereço (EnderecoOutros_tpEndereco) inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "EnderecoOutrosTpEndereco":
        return cls(val)

    def __str__(self):
        return self.value if self.value is not None else ""


class EnderecoOutrosEnderecoLivre:
    """Endereço na forma de texto livre"""
    def __init__(self, value: str):
        # minOccurs: 0, maxLength: 200; opcional
        if value is not None and not (1 <= len(value) <= 200):
            raise ValueError("EnderecoOutros_EnderecoLivre inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "EnderecoOutrosEnderecoLivre":
        return cls(val)

    def __str__(self):
        return self.value if self.value is not None else ""


class EnderecoEstruturaEnderecoLivre:
    """Parte do endereço estruturado na forma de texto livre"""
    def __init__(self, value: str):
        # minOccurs: 0, maxLength: 200; opcional
        if value is not None and not (1 <= len(value) <= 200):
            raise ValueError("EnderecoEstrutura_EnderecoLivre inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "EnderecoEstruturaEnderecoLivre":
        return cls(val)

    def __str__(self):
        return self.value if self.value is not None else ""


class Logradouro:
    """Logradouro"""
    def __init__(self, value: str):
        # minOccurs: 0, maxLength: 60; opcional
        if value is not None and not (1 <= len(value) <= 60):
            raise ValueError("Logradouro inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Logradouro":
        return cls(val)

    def __str__(self):
        return self.value if self.value is not None else ""


class Numero:
    """Número(ou outra identificação) no logradouro"""
    def __init__(self, value: str):
        # minOccurs: 0, maxLength: 10; opcional
        if value is not None and not (1 <= len(value) <= 10):
            raise ValueError("Número inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Numero":
        return cls(val)

    def __str__(self):
        return self.value if self.value is not None else ""


class Complemento:
    """Subunidade no local identificado pelo logradouro/número"""
    def __init__(self, value: str):
        # minOccurs: 0, maxLength: 10; opcional
        if value is not None and not (1 <= len(value) <= 10):
            raise ValueError("Complemento inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Complemento":
        return cls(val)

    def __str__(self):
        return self.value if self.value is not None else ""


class Andar:
    """Andar da subunidade no local identificado pelo logradouro/número"""
    def __init__(self, value: str):
        # minOccurs: 0, maxLength: 10; opcional
        if value is not None and not (1 <= len(value) <= 10):
            raise ValueError("Andar inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Andar":
        return cls(val)

    def __str__(self):
        return self.value if self.value is not None else ""


class Bairro:
    """Bairro(ou alguma outra subdivisão da cidade)"""
    def __init__(self, value: str):
        # minOccurs: 0, maxLength: 40; opcional
        if value is not None and not (1 <= len(value) <= 40):
            raise ValueError("Bairro inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Bairro":
        return cls(val)

    def __str__(self):
        return self.value if self.value is not None else ""


class CaixaPostal:
    """Código de Caixa postal"""
    def __init__(self, value: str):
        # minOccurs: 0, maxLength: 12; opcional
        if value is not None and not (1 <= len(value) <= 12):
            raise ValueError("Caixa Postal inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "CaixaPostal":
        return cls(val)

    def __str__(self):
        return self.value if self.value is not None else ""


class EnderecoEstruturaCEP:
    """Código de Endereçamento Postal do endereço"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 12):
            raise ValueError("CEP do endereço estruturado inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "EnderecoEstruturaCEP":
        return cls(val)

    def __str__(self):
        return self.value


class EnderecoEstruturaMunicipio:
    """Município brasileiro, ou cidade no exterior"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 60):
            raise ValueError("Município do endereço estruturado inválido")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "EnderecoEstruturaMunicipio":
        return cls(val)

    def __str__(self):
        return self.value


class EnderecoEstruturaUF:
    """Unidade da Federação Brasileira (sigla) ou subdivisão do país estrangeiro"""
    def __init__(self, value: str):
        if not value or not (1 <= len(value) <= 40):
            raise ValueError("UF do endereço estruturado inválida")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "EnderecoEstruturaUF":
        return cls(val)

    def __str__(self):
        return self.value


class Signature:
    """Assinatura digital (ds:Signature)"""
    def __init__(self, value: str):
        # Considera-se que o conteúdo da assinatura seja uma string;
        # a validação específica deve ser implementada conforme necessidade.
        if not value:
            raise ValueError("Signature inválida")
        self.value = value

    @classmethod
    def from_str(cls, val: str) -> "Signature":
        return cls(val)

    def __str__(self):
        return self.value

# =============================================================================
#                               ENTIDADES
# =============================================================================

class EFinanceira:
    """Elemento raiz do eFinanceira"""
    def __init__(self, evt_cad_declarante: "EvtCadDeclarante", signature: Signature):
        self.evt_cad_declarante = evt_cad_declarante
        self.signature = signature


class EvtCadDeclarante:
    """Evento de Informações da Entidade Declarante"""
    def __init__(self,
                 id: ID,
                 ide_evento: "IdeEvento",
                 ide_declarante: "IdeDeclarante",
                 info_cadastro: "InfoCadastro"):
        self.id = id
        self.ide_evento = ide_evento
        self.ide_declarante = ide_declarante
        self.info_cadastro = info_cadastro


class IdeEvento:
    """Informações de Identificação do Evento"""
    def __init__(self,
                 ind_retificacao: IndRetificacao,
                 tp_amb: TpAmb,
                 aplic_emi: AplicEmi,
                 ver_aplic: VerAplic,
                 nr_recibo: Optional[NumeroRecibo] = None):
        # nrRecibo é opcional (minOccurs=0)
        self.ind_retificacao = ind_retificacao
        self.nr_recibo = nr_recibo
        self.tp_amb = tp_amb
        self.aplic_emi = aplic_emi
        self.ver_aplic = ver_aplic


class IdeDeclarante:
    """Informações de identificação da Entidade Declarante"""
    def __init__(self, cnpj_declarante: CnpjDeclarante):
        self.cnpj_declarante = cnpj_declarante


class InfoCadastro:
    """Informações de cadastro da Entidade Declarante"""
    def __init__(self,
                 nome: Nome,
                 endereco_livre: EnderecoLivre,
                 municipio: Municipio,
                 uf: UF,
                 cep: CEP,
                 pais: Pais,
                 giin: Optional[GIIN] = None,
                 categoria_declarante: Optional[CategoriaDeclarante] = None,
                 info_tp_inst_pgto1: Optional["InfoTpInstPgto1"] = None,
                 nif1: Optional["NIF1"] = None,
                 tp_nome: Optional[TpNome] = None,
                 tp_endereco: Optional[TpEndereco] = None,
                 pais_resid1: Optional["PaisResid1"] = None,
                 endereco_outros1: Optional["EnderecoOutros1"] = None):
        self.giin = giin
        self.categoria_declarante = categoria_declarante
        self.info_tp_inst_pgto1 = info_tp_inst_pgto1
        self.nif1 = nif1
        self.nome = nome
        self.tp_nome = tp_nome
        self.endereco_livre = endereco_livre
        self.tp_endereco = tp_endereco
        self.municipio = municipio
        self.uf = uf
        self.cep = cep
        self.pais = pais
        self.pais_resid1 = pais_resid1
        self.endereco_outros1 = endereco_outros1


class InfoTpInstPgto1:
    """Informações do tipos de instituições de pagamento operados pelo declarante"""
    def __init__(self, tp_inst_pgto: TpInstPgto):
        self.tp_inst_pgto = tp_inst_pgto


class NIF1:
    """Informações de identificação fiscal no exterior da Entidade Declarante"""
    def __init__(self,
                 numero_nif: NumeroNIF,
                 pais_emissao: PaisEmissao,
                 tp_nif: Optional[TpNIF] = None):
        self.numero_nif = numero_nif
        self.pais_emissao = pais_emissao
        self.tp_nif = tp_nif


class PaisResid1:
    """País de residência fiscal da Entidade Declarante"""
    def __init__(self, pais_resid_pais: PaisResidPais):
        self.pais_resid_pais = pais_resid_pais


class EnderecoOutros1:
    """Demais endereços da Entidade Declarante"""
    def __init__(self,
                 endereco_outros_tp_endereco: Optional[EnderecoOutrosTpEndereco] = None,
                 endereco_outros_endereco_livre: Optional[EnderecoOutrosEnderecoLivre] = None,
                 endereco_outros_endereco_estrutura: Optional["EnderecoOutrosEnderecoEstrutura"] = None):
        self.endereco_outros_tp_endereco = endereco_outros_tp_endereco
        self.endereco_outros_endereco_livre = endereco_outros_endereco_livre
        self.endereco_outros_endereco_estrutura = endereco_outros_endereco_estrutura


class EnderecoOutrosEnderecoEstrutura:
    """Endereço na forma estruturada"""
    def __init__(self,
                 endereco_estrutura_endereco_livre: Optional[EnderecoEstruturaEnderecoLivre] = None,
                 endereco: Optional["Endereco"] = None,
                 endereco_estrutura_cep: EnderecoEstruturaCEP = None,
                 endereco_estrutura_municipio: EnderecoEstruturaMunicipio = None,
                 endereco_estrutura_uf: EnderecoEstruturaUF = None):
        self.endereco_estrutura_endereco_livre = endereco_estrutura_endereco_livre
        self.endereco = endereco
        self.endereco_estrutura_cep = endereco_estrutura_cep
        self.endereco_estrutura_municipio = endereco_estrutura_municipio
        self.endereco_estrutura_uf = endereco_estrutura_uf


class Endereco:
    """Dados do endereço"""
    def __init__(self,
                 logradouro: Optional[Logradouro] = None,
                 numero: Optional[Numero] = None,
                 complemento: Optional[Complemento] = None,
                 andar: Optional[Andar] = None,
                 bairro: Optional[Bairro] = None,
                 caixa_postal: Optional[CaixaPostal] = None):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.andar = andar
        self.bairro = bairro
        self.caixa_postal = caixa_postal

