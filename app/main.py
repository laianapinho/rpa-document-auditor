# Importa as configurações principais do projeto.
from app.config import APP_NAME, INPUT_DIR, OUTPUT_DIR, LOG_DIR, EVIDENCE_DIR

# Importa a função responsável por listar os documentos válidos da pasta de entrada.
from app.file_service import listar_documentos_validos

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

    documentos_validos = listar_documentos_validos(INPUT_DIR)

    # Exibe a quantidade de documentos válidos encontrados.
    print(f"Quantidade de documentos válidos: {len(documentos_validos)}")

    # Exibe uma linha final.
    print("=" * 60)


# Garante que a função main será executada apenas quando este arquivo for rodado diretamente.
if __name__ == "__main__":
    main()