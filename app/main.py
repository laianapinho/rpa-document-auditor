# Importa as configurações principais do projeto.
from app.config import APP_NAME, INPUT_DIR, OUTPUT_DIR, LOG_DIR, EVIDENCE_DIR

# Importa a função responsável por listar os documentos válidos da pasta de entrada.
from app.file_service import listar_documentos_validos
from app.ocr_service import extrair_texto_documento
from app.extractor_service import extrair_campos_documento

def main():
    # Exibe uma mensagem inicial no terminal.
    print("=" * 60)

    # Exibe o nome da aplicação.
    print(f"Iniciando projeto: {APP_NAME}")

    # Exibe a pasta de entrada dos documentos.
    print(f"Pasta de entrada: {INPUT_DIR}")

    # Exibe a pasta de saída dos relatórios.
    print(f"Pasta de saída: {OUTPUT_DIR}")

    # Exibe a pasta de logs.
    print(f"Pasta de logs: {LOG_DIR}")

    # Exibe a pasta de evidências.
    print(f"Pasta de evidências: {EVIDENCE_DIR}")

    # Exibe uma mensagem de sucesso.
    print("Estrutura inicial carregada com sucesso.")

   # Chama a função que lista os documentos válidos dentro da pasta de entrada.
# O retorno será uma lista com arquivos aceitos, como PDF, PNG, JPG e JPEG.
    documentos_validos = listar_documentos_validos(INPUT_DIR)

# Percorre cada documento encontrado na lista de documentos válidos.
# A variável "documento" representa um arquivo por vez.
    for documento in documentos_validos:

    # Imprime uma linha separadora para organizar a saída no terminal.
        print("-" * 60)

    # Mostra o nome do documento que está sendo processado no momento.
        print(f"Documento: {documento.name}")

    # Extrai o texto bruto do documento atual.
    # Se for PDF, usa o PyMuPDF.
    # Se for imagem, usa OCR com Tesseract.
        texto = extrair_texto_documento(documento)
        #print(texto)

    # Envia o texto bruto para a função que extrai os campos importantes.
    # Essa função retorna um dicionário com valor, data, tipo, instituição, nome e CPF/CNPJ.
        campos = extrair_campos_documento(texto)

    # Imprime no terminal o dicionário com os campos extraídos do documento.
        print(campos)


# Garante que a função main será executada apenas quando este arquivo for rodado diretamente.
if __name__ == "__main__":
    main()