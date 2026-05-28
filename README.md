# RPA Document Auditor

Projeto de automação RPA desenvolvido em Python para auditoria automática de documentos.

A proposta é simular um robô capaz de ler documentos, extrair informações importantes, validar campos obrigatórios, organizar arquivos por situação e gerar relatórios finais com evidências do processamento.

---

## Objetivo do projeto

O objetivo do **RPA Document Auditor** é criar uma automação que auxilie na auditoria documental, reduzindo tarefas manuais repetitivas e aumentando a rastreabilidade do processo.

O projeto será desenvolvido de forma progressiva, por dias, simulando uma rotina real de construção de uma solução RPA.

---

## Funcionalidades planejadas

- Leitura de documentos em uma pasta de entrada.
- Identificação de arquivos válidos e inválidos.
- Extração de texto de PDFs e imagens.
- Uso de OCR para leitura de documentos digitalizados.
- Extração de campos como nome, CPF, valor, data e status.
- Validação automática dos dados extraídos.
- Organização dos documentos em pastas de processados, pendentes e erros.
- Geração de relatório em Excel.
- Registro de logs da execução.
- Salvamento de evidências.
- Possível integração com BotCity para execução e orquestração do robô.

---

## Tecnologias utilizadas

- Python 3.11
- BotCity
- Pytesseract
- Pillow
- PyMuPDF
- OpenCV
- Pandas
- OpenPyXL
- Python-dotenv

---

## Estrutura inicial do projeto

```text
rpa-document-auditor/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── logger_config.py
│   ├── ocr_service.py
│   ├── extractor_service.py
│   ├── validator_service.py
│   ├── file_service.py
│   └── report_service.py
│
├── data/
│   ├── input/
│   ├── processed/
│   ├── pending/
│   └── error/
│
├── evidences/
├── logs/
├── output/
├── samples/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Como executar o projeto

### 1. Clonar ou criar a pasta do projeto

```bash
mkdir rpa-document-auditor
cd rpa-document-auditor
```

---

### 2. Criar o ambiente virtual com Python 3.11

No Windows, use:

```bash
py -3.11 -m venv venv
```

---

### 3. Ativar o ambiente virtual

No PowerShell:

```bash
venv\Scripts\activate
```

---

### 4. Conferir a versão do Python

```bash
python --version
```

O esperado é algo parecido com:

```text
Python 3.11.x
```

---

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 6. Executar o projeto

```bash
python -m app.main
```

---

## Dependências iniciais

O arquivo `requirements.txt` deve conter:

```txt
botcity-framework-core
botcity-framework-web
botcity-maestro-sdk
pytesseract
pillow
pymupdf
opencv-python
pandas
openpyxl
python-dotenv
```

---

## Variáveis de ambiente

O arquivo `.env.example` deve conter:

```env
APP_NAME=RPA Document Auditor
INPUT_DIR=data/input
PROCESSED_DIR=data/processed
PENDING_DIR=data/pending
ERROR_DIR=data/error
OUTPUT_DIR=output
LOG_DIR=logs
EVIDENCE_DIR=evidences
```

---

## Arquivos de exemplo

No Dia 1, foram criados documentos fictícios em formato `.txt` dentro da pasta `samples/`.

Esses arquivos simulam comprovantes de pagamento e serão usados posteriormente para testar a extração e validação dos dados.

Exemplo de documento:

```text
COMPROVANTE DE PAGAMENTO

Nome: Ana Silva
CPF: 123.456.789-00
Valor: R$ 250,00
Data: 20/05/2026
Status: Pago
```

---

## Status do projeto

Projeto iniciado.

### Dia 1 concluído

Atividades realizadas:

- Criação da pasta principal do projeto.
- Criação do ambiente virtual com Python 3.11.
- Criação da estrutura inicial de diretórios.
- Criação dos arquivos principais da aplicação.
- Configuração inicial do `requirements.txt`.
- Configuração inicial do `.gitignore`.
- Configuração inicial do `.env.example`.
- Criação do arquivo `config.py`.
- Criação do arquivo `main.py`.
- Criação de documentos fictícios para testes.
- Primeiro teste de execução no terminal.

---

## Próximos passos

No Dia 2, será implementada a listagem dos documentos da pasta `data/input`.

A partir do Dia 2, o desenvolvimento será feito em formato de mentoria prática:

1. Primeiro será explicado o objetivo do dia.
2. Depois será apresentada a lógica que precisa ser implementada.
3. O código completo só será fornecido caso haja dificuldade ou erro na implementação.
4. Ao final, haverá um mini desafio para treino.

---

## Autor

Projeto desenvolvido por Laiana como parte dos estudos em RPA, automação de processos e BotCity.
