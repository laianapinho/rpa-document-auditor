# Importa a classe Path para trabalhar com caminhos de arquivos e pastas.
from pathlib import Path

# Importa a classe Image da biblioteca Pillow para abrir imagens.
from PIL import Image

# Importa o pytesseract, que permite usar o Tesseract OCR pelo Python.
import pytesseract

# Importa o PyMuPDF, usado para abrir e extrair texto de arquivos PDF.
import fitz


# Define manualmente o caminho do executável do Tesseract no Windows.
# Isso ajuda quando o Tesseract está instalado, mas não está configurado no PATH.
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Define uma função para extrair texto de imagens.
def extrair_texto_imagem(arquivo_path):
    # Abre a imagem usando a biblioteca Pillow.
    imagem = Image.open(arquivo_path)

    # Usa o Tesseract OCR para extrair texto da imagem.
    # Por enquanto, não usamos lang="por" para evitar erro caso o idioma português não esteja instalado.
    texto = pytesseract.image_to_string(imagem)

    # Fecha a imagem após o uso.
    imagem.close()

    # Retorna o texto extraído da imagem.
    return texto


# Define uma função para extrair texto de PDF.
def extrair_texto_pdf(arquivo_path):
    # Abre o arquivo PDF usando o PyMuPDF.
    documento_pdf = fitz.open(arquivo_path)

    # Cria uma variável vazia para acumular o texto de todas as páginas.
    texto_final = ""

    # Percorre todas as páginas do PDF.
    for pagina in documento_pdf:
        # Extrai o texto da página atual.
        texto_da_pagina = pagina.get_text()

        # Adiciona o texto da página ao texto final com quebra de linha.
        texto_final += texto_da_pagina + "\n"

    # Fecha o PDF após a leitura.
    documento_pdf.close()

    # Retorna o texto completo extraído do PDF.
    return texto_final


# Define uma função principal para extrair texto de qualquer documento suportado.
def extrair_texto_documento(caminho_arquivo):
    # Converte o caminho recebido para um objeto Path.
    arquivo_path = Path(caminho_arquivo)

    # Verifica se o arquivo existe.
    if not arquivo_path.exists():
        # Mostra uma mensagem de erro caso o arquivo não exista.
        print(f"Erro: o arquivo '{arquivo_path}' não existe.")

        # Retorna texto vazio para evitar quebra no programa.
        return ""

    # Pega a extensão do arquivo em letras minúsculas.
    extensao = arquivo_path.suffix.lower()

    # Verifica se o arquivo é uma imagem.
    if extensao in [".png", ".jpg", ".jpeg"]:
        # Chama a função responsável por extrair texto de imagem.
        return extrair_texto_imagem(arquivo_path)

    # Verifica se o arquivo é PDF.
    elif extensao == ".pdf":
        # Chama a função responsável por extrair texto de PDF.
        return extrair_texto_pdf(arquivo_path)

    # Caso a extensão não seja suportada.
    else:
        # Mostra uma mensagem informando que o tipo de arquivo não é suportado.
        print(f"Extensão não suportada: {extensao}")

        # Retorna texto vazio.
        return ""