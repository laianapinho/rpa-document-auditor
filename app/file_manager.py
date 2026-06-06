import os
import shutil

# Define a função que recebe o caminho do arquivo e o status do documento.
# Ela irá mover o arquivo para a pasta correspondente ao seu status.
def mover_arquivos(caminho_arquivo, status):
    # Se o status for "Conforme", define a pasta de destino como "data/conforme".
    if status=="Conforme":
        pasta_destino = "data/conforme"
    elif status=="Pendente":
        pasta_destino = "data/pendente"
    else:
        pasta_destino = "data/erro"

    # Cria a pasta de destino caso ela não exista.
    # exist_ok=True evita que o Python lance um erro se a pasta já existir.
    os.makedirs(pasta_destino, exist_ok=True)

    # Move o arquivo do caminho original para a pasta de destino.
    # Isso reorganiza os documentos de acordo com seu status.
    shutil.move(caminho_arquivo, pasta_destino)

    return pasta_destino

