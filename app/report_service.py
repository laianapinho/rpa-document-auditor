# Importa bibliotecas para manipulação de dados e arquivos
import pandas as pd
from pathlib import Path
from datetime import datetime

# Importa funções e configurações do projeto
from app.config import APP_NAME, INPUT_DIR, OUTPUT_DIR, LOG_DIR, EVIDENCE_DIR
from app.file_service import listar_documentos_validos
from app.ocr_service import extrair_texto_documento
from app.extractor_service import extrair_campos_documento
from app.validator_service import validar_campos_documento
from app.file_manager import mover_arquivos

# Inicializa uma lista vazia para armazenar os resultados de todos os documentos processados
resultados = []

# Função que cria o relatório Excel a partir da lista de resultados
def relatorio_documento(resultados):
    """
    Gera um relatório em Excel com os campos extraídos, status e pendências de cada documento.
    
    Parâmetros:
    resultados (list): lista de dicionários com os dados de cada documento
    """
    # Transforma a lista de dicionários em um DataFrame do pandas
    df = pd.DataFrame(resultados)
    
   # Gera timestamp atual no formato YYYYMMDD_HHMMSS
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Define o caminho do relatório com timestamp
    caminho_saida = Path(f"reports/relatorio_{timestamp}.xlsx")
    
    # Garante que a pasta 'reports/' exista; cria se necessário
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    
    # Salva o DataFrame como arquivo Excel
    # index=False evita que o pandas crie uma coluna extra de índices
    df.to_excel(caminho_saida, index=False)
    
    # Retorna o caminho de saída caso queira usar depois
    return caminho_saida
