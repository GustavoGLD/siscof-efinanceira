# SISCOF e-Financeira

## 🏦 Visão Geral

O **SISCOF e-Financeira** é uma ferramenta projetada para facilitar o cumprimento das obrigações legais de relatórios financeiros eletrônicos (e-Financeira) exigidos pela Receita Federal do Brasil ([Receita Federal](http://sped.rfb.gov.br/projeto/show/1179)). O sistema permite a criação, validação e gerenciamento de arquivos XML que seguem os padrões estabelecidos para a e-Financeira, abrangendo funcionalidades como cadastro de patrocinados e intermediários, exclusão de registros, fechamento de períodos contábeis e geração de relatórios de movimentação financeira.

Desenvolvido com foco em eficiência e conformidade, o projeto utiliza Python como linguagem principal e inclui esquemas XML para garantir a integridade dos dados reportados.

## 🚀 Funcionalidades Principais

O sistema oferece as seguintes funcionalidades principais, baseadas na estrutura de pastas e arquivos do repositório:

- **Cadastro de Patrocinado**: Permite o cadastro de patrocinados no sistema e-Financeira.
- **Cadastro de Intermediário**: Permite o cadastro de intermediários no sistema e-Financeira.
- **Exclusão**: Funcionalidade para excluir registros no sistema e-Financeira.
- **Exclusão e-Financeira**: Exclusão específica de registros relacionados à e-Financeira.
- **Fechamento**: Realiza o fechamento de períodos contábeis ou operações financeiras.
- **Movimento de Operações Financeiras Anual**: Gera relatórios ou movimentações anuais de operações financeiras.
- **Movimento de Operações Financeiras**: Gera relatórios ou movimentações de operações financeiras em períodos mais curtos.

## 📷 Imagens

![image](https://github.com/user-attachments/assets/29e4fd05-85c4-4091-9a62-ebd2d54744b5)
![image](https://github.com/user-attachments/assets/758a16f6-95c1-4a6b-87e6-df6f388dffee)


## 🗂 Arquitetura & Estrutura de Código

O projeto é organizado em várias pastas, cada uma com um propósito específico:

| Pasta/Subpasta | Descrição |
|----------------|-----------|
| **diagramas** | Contém diagramas que ilustram a estrutura ou o fluxo do sistema. |
| **schemas** | Contém os esquemas XML utilizados para validar os arquivos de e-Financeira. |
| **subschemas** | Contém subschemas ou componentes menores dos esquemas XML. |
| **source** | Contém o código-fonte em Python, organizado em módulos para cada funcionalidade: |
| &nbsp;&nbsp; `cadastrar_patrocinado` | Módulo para cadastro de patrocinados. |
| &nbsp;&nbsp; `cadastro_intermediario` | Módulo para cadastro de intermediários. |
| &nbsp;&nbsp; `exclusao` | Módulo para exclusão de registros. |
| &nbsp;&nbsp; `exclusao_efinanceira` | Módulo específico para exclusão relacionada à e-Financeira. |
| &nbsp;&nbsp; `fechamento` | Módulo para fechamento de períodos. |
| &nbsp;&nbsp; `mov_op_fin_anual` | Módulo para movimentos anuais de operações financeiras. |
| &nbsp;&nbsp; `mov_ov_fin` | Módulo para movimentos de operações financeiras. |
| **tests** | Contém testes unitários para validar as funcionalidades implementadas. |

Além disso, há arquivos como `generate_evt.py` e `generate_xsds.py`, que são utilizados para gerar eventos e esquemas XML, respectivamente.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do sistema.
- **XML**: Utilizado para a estruturação dos dados de e-Financeira, com base nos esquemas fornecidos.
- **xml.etree.ElementTree** e **lxml**: manipulação de XML.

## ⚙️ Instalação e Configuração

1. **Clone o repositório**

   ```bash
   git clone https://github.com/GustavoGLD/siscof-efinanceira.git
   cd siscof-efinanceira
   ```

2. **Crie e ative um ambiente virtual**

   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

   *Certifique-se de que o arquivo `requirements.txt` esteja presente no repositório com as dependências listadas.*

4. **Configure as variáveis de ambiente**

   *Se necessário, configure variáveis de ambiente para chaves de API ou outras configurações sensíveis, conforme exigido pela integração com serviços da Receita Federal.*

5. **Execute o aplicativo**

   *Dependendo da estrutura do projeto, execute o script principal ou use um comando específico, como `python generate_evt.py` para gerar eventos.*

## 👩‍💻 Como Usar

Para usar o sistema, você pode executar os scripts Python correspondentes a cada funcionalidade. Exemplos incluem:

- **Cadastro de Patrocinado**: `python source/cadastrar_patrocinado/builders.py`
- **Cadastro de Intermediário**: `python source/cadastro_intermediario/builders.py`
- **Geração de Eventos**: `python generate_evt.py`

*Nota: Os comandos exatos podem variar dependendo da implementação. Consulte a documentação específica de cada módulo ou script para detalhes.*

## 🔍 Testes

O projeto inclui testes unitários localizados na pasta `tests`. Para executar os testes, use:

```bash
python -m unittest discover -s tests
```

*Ou utilize outra ferramenta de teste, como `pytest`, se configurada no projeto.*

## 🚧 Trabalhos Futuros

- Adicionar suporte a mais funcionalidades da e-Financeira, como relatórios adicionais.
- Melhorar a documentação com exemplos detalhados de uso.
- Implementar uma interface gráfica para facilitar a interação com o sistema.
- Integrar validações automáticas para garantir conformidade com as atualizações da Receita Federal.

## 🔍 Desafios & Aprendizados

- **Manipulação de XML**: Trabalhar com esquemas XML complexos exigiu um entendimento profundo das especificações da e-Financeira.
- **Conformidade Regulatória**: Garantir que os arquivos gerados atendam aos padrões da Receita Federal foi um desafio crítico.
- **Modularidade**: A organização do código em módulos separados facilitou a manutenção e a escalabilidade do sistema.
- **Testes Unitários**: A implementação de testes unitários ajudou a garantir a robustez das funcionalidades.

**Autor:** Gustavo Lídio Damaceno • [LinkedIn](https://www.linkedin.com/in/gustavo-lidio-damaceno/)

- [Receita Federal - Informações sobre e-Financeira](http://sped.rfb.gov.br/projeto/show/1179)
- [Contabilidade no Brasil - Explicação sobre e-Financeira](https://www.contabilidadenobrasil.com.br/e-financeira/)
