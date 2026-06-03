# Define a função que recebe os campos extraídos de um documento
# e retorna se o documento está conforme ou pendente, junto com uma lista de pendências.
def validar_campos_documento(campos):

    # Cria uma lista vazia para armazenar as pendências encontradas.
    pendencias = []

    # Verifica se o campo "valor" está vazio ou não existe.
    # Se estiver vazio, adiciona uma mensagem de pendência.
    #verificação se um campo do dicionários campos é vazio
    if not campos.get("valor"):
        pendencias.append("Valor não encontrado")

    # Verifica se o campo "data" está vazio ou não existe.
    # Se estiver vazio, adiciona uma mensagem de pendência.
    if not campos.get("data"):
        pendencias.append("Data não encontrada")

    # Verifica se o campo "nome" está vazio ou não existe.
    # Se estiver vazio, adiciona uma mensagem de pendência.
    if not campos.get("nome"):
        pendencias.append("Nome não encontrado")

    # Verifica se o campo "cpf_cnpj" está vazio ou não existe.
    # Se estiver vazio, adiciona uma mensagem de pendência.
    if not campos.get("cpf_cnpj"):
        pendencias.append("CPF/CNPJ não encontrado")

    # Se a lista de pendências estiver vazia, significa que todos os campos obrigatórios foram encontrados.
    # Então o status do documento é "Conforme".
    #verifica se uma lista é vazia
    if not pendencias:
        status = "Conforme"
    # Caso contrário, algum campo obrigatório está faltando, e o status é "Pendente".
    else:
        status = "Pendente"

    # Retorna um dicionário contendo o status do documento
    # e a lista de pendências encontradas (pode estar vazia).
    return {
        "status": status,
        "pendencias": pendencias,
    }