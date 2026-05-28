# Importa a biblioteca os para lidar com variáveis de ambiente.
import os

# Importa load_dotenv para carregar variáveis do arquivo .env, caso exista.
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env.
load_dotenv()

# Nome da aplicação.
APP_NAME = os.getenv("APP_NAME", "RPA Document Auditor")

# Pasta onde ficam os documentos que serão processados.
INPUT_DIR = os.getenv("INPUT_DIR", "data/input")

# Pasta onde ficam os documentos conformes.
PROCESSED_DIR = os.getenv("PROCESSED_DIR", "data/processed")

# Pasta onde ficam os documentos pendentes.
PENDING_DIR = os.getenv("PENDING_DIR", "data/pending")

# Pasta onde ficam os documentos com erro.
ERROR_DIR = os.getenv("ERROR_DIR", "data/error")

# Pasta onde serão salvos os relatórios.
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")

# Pasta onde serão salvos os logs.
LOG_DIR = os.getenv("LOG_DIR", "logs")

# Pasta onde serão salvas as evidências.
EVIDENCE_DIR = os.getenv("EVIDENCE_DIR", "evidences")