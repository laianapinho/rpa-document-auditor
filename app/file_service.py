# Importa a classe Path para trabalhar com caminhos de arquivos e pastas.
from pathlib import Path

from app.config import APP_NAME, INPUT_DIR, OUTPUT_DIR, LOG_DIR, EVIDENCE_DIR
# Define uma função chamada listar_documentos_validos.
# Essa função recebe como parâmetro o caminho da pasta onde estão os documentos.
def listar_documentos_validos(input_dir):

    # Converte o caminho recebido para um objeto Path.
    # Isso permite usar métodos como exists(), iterdir(), is_file() e suffix.
    input_path = Path(input_dir)

    # Verifica se a pasta informada não existe.
    if not input_path.exists():

        # Mostra uma mensagem de erro informando que o caminho não foi encontrado.
        print(f"Erro: O caminho '{input_path}' não existe.")

        # Retorna uma lista vazia para evitar erro no restante do programa.
        return []

    # Cria um conjunto com as extensões de arquivos permitidas no projeto.
    # Apenas arquivos com essas extensões serão considerados válidos.
    extensoes_permitidas = {'.pdf', '.png', '.jpg', '.jpeg'}

    # Cria uma lista vazia para guardar os arquivos aceitos.
    arquivos_aceitos = []

    # Percorre todos os itens encontrados dentro da pasta de entrada.
    for item in input_path.iterdir():

        # Verifica se o item atual é um arquivo.
        # Isso evita tentar processar pastas como se fossem documentos.
        if item.is_file():

            # Pega a extensão do arquivo atual.
            # O lower() converte para minúsculo, aceitando casos como .PDF ou .JPG.
            extensao = item.suffix.lower()

            # Verifica se a extensão do arquivo está entre as extensões permitidas.
            if extensao in extensoes_permitidas:

                # Exibe no terminal que o arquivo foi aceito.
                print(f"✅ Aceito: {item.name} (Tipo: {extensao})")

                # Adiciona o arquivo aceito na lista de arquivos válidos.
                arquivos_aceitos.append(item)

            # Caso a extensão não esteja entre as permitidas, o arquivo será ignorado.
            else:

                # Exibe no terminal que o arquivo foi ignorado.
                print(f"❌ Ignorado: {item.name} (Extensão {extensao} não permitida)")

    # Exibe no terminal o total de arquivos válidos encontrados.
    print(f"\nTotal de arquivos válidos encontrados: {len(arquivos_aceitos)}")

    # Retorna a lista com os arquivos válidos encontrados.
    return arquivos_aceitos