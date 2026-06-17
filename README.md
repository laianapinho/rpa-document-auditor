# RPA Document Auditor – Versão Final

## Descrição do Projeto
O **RPA Document Auditor** é um sistema de automação para processar comprovantes de transações financeiras (PDFs e imagens), extrair campos importantes, validar dados obrigatórios, organizar arquivos por status e gerar relatórios consolidados em Excel.

O projeto funciona totalmente localmente, sem dependência de plataformas externas como BotCity.

---

## Funcionalidades Principais
- Listar documentos válidos na pasta `data/input` (PDF, PNG, JPG, JPEG).
- Extrair texto de PDFs (PyMuPDF) e imagens (OCR com Tesseract).
- Extrair campos importantes: `valor`, `data`, `tipo`, `instituicao`, `nome`, `cpf_cnpj`.
- Validar campos obrigatórios e gerar status (`Conforme` ou `Pendente`) e lista de pendências.
- Mover arquivos automaticamente para pastas `data/conforme`, `data/pendente` ou `data/erro`.
- Gerar relatório Excel consolidado (`reports/`) com timestamp.
- Todo o processo é executado pelo script `main.py`.

---

## Estrutura do Projeto
```text
RPA-Document-Auditor/
├─ app/
│  ├─ config.py
│  ├─ file_service.py
│  ├─ ocr_service.py
│  ├─ extractor_service.py
│  ├─ validator_service.py
│  ├─ file_manager.py
│  ├─ report_service.py
├─ data/
│  ├─ input/         # Comprovantes para processar
│  ├─ conforme/      # Documentos sem pendências
│  ├─ pendente/      # Documentos com pendências
│  ├─ erro/          # Arquivos corrompidos ou não processáveis
├─ reports/          # Relatórios Excel gerados
├─ main.py           # Pipeline principal
├─ README.md         # Este arquivo
```

---

## Requisitos
- Python 3.11
- Bibliotecas:
  - pandas
  - pathlib
  - datetime
  - PyMuPDF
  - pytesseract
  - Pillow
- Tesseract OCR instalado no sistema e caminho configurado no `ocr_service.py`.

---

## Execução do Pipeline
1. Coloque os comprovantes na pasta `data/input/`.
2. Abra o terminal no diretório do projeto.
3. Ative o ambiente virtual Python.
4. Rode:

```bash
python -m app.main
```

5. O script irá:
   - Processar cada arquivo.
   - Extrair e validar campos.
   - Mover arquivos para a pasta correta.
   - Gerar relatório Excel em `reports/` com timestamp.

---

## Estrutura do Relatório

O relatório Excel contém as colunas:

- valor
- data
- tipo
- instituicao
- nome
- cpf_cnpj
- status
- pendencias

Cada linha representa um documento processado.

---

## Observações

- Qualquer arquivo que não seja PDF, PNG, JPG ou JPEG será ignorado.
- Arquivos problemáticos ou vazios serão movidos para `data/erro/`.
- Este projeto está pronto para rodar totalmente local, sem BotCity.
