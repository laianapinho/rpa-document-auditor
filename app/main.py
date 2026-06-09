# Importa bibliotecas e módulos do projeto
import pandas as pd
from pathlib import Path

from app.config import APP_NAME, INPUT_DIR, OUTPUT_DIR, LOG_DIR, EVIDENCE_DIR
from app.file_service import listar_documentos_validos
from app.ocr_service import extrair_texto_documento
from app.extractor_service import extrair_campos_documento
from app.validator_service import validar_campos_documento
from app.file_manager import mover_arquivos
from app.report_service import relatorio_documento

def main():
    # --- Mensagens iniciais ---
    print("=" * 60)
    print(f"Iniciando projeto: {APP_NAME}")
    print(f"Pasta de entrada: {INPUT_DIR}")
    print(f"Pasta de saída: {OUTPUT_DIR}")
    print(f"Pasta de logs: {LOG_DIR}")
    print(f"Pasta de evidências: {EVIDENCE_DIR}")
    print("Estrutura inicial carregada com sucesso.")

    # --- Lista de documentos válidos ---
    documentos_validos = listar_documentos_validos(INPUT_DIR)

    # --- Lista que vai armazenar os resultados de todos os documentos ---
    resultados = []

    # --- Processamento de cada documento ---
    for documento in documentos_validos:
        print("-" * 60)
        print(f"Documento: {documento.name}")

        # 1️⃣ Extrai texto do documento
        texto = extrair_texto_documento(documento)
        
        # 2️⃣ Extrai campos importantes do texto
        campos = extrair_campos_documento(texto)
        print(campos)

        # 3️⃣ Valida os campos obrigatórios
        verificacao = validar_campos_documento(campos)
        print(verificacao["status"])
        print(verificacao["pendencias"])

        # 4️⃣ Move o arquivo para a pasta correspondente ao status
        pasta_destino = mover_arquivos(documento, verificacao["status"])
        print(f"{documento.name} movido para {pasta_destino}")

        # 5️⃣ Cria o dicionário de resultados do documento
        dicionario_documento = {
            "valor": campos["valor"],
            "data": campos["data"],
            "tipo": campos["tipo"],
            "instituicao": campos["instituicao"],
            "nome": campos["nome"],
            "cpf_cnpj": campos["cpf_cnpj"],
            "status": verificacao["status"],
            "pendencias": ", ".join(verificacao["pendencias"])
        }

        # 6️⃣ Adiciona o dicionário à lista de resultados
        resultados.append(dicionario_documento)

    # --- Gera o relatório Excel consolidado após processar todos os documentos ---
    relatorio_documento(resultados)

# Garante que a função main será executada apenas quando este arquivo for rodado diretamente
if __name__ == "__main__":
    main()