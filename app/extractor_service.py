import re

# Cria uma variável chamada valor com o padrão regex para encontrar valores em reais.
# O r antes das aspas indica uma raw string, ou seja, uma string bruta.
# Isso evita problemas com barras invertidas dentro da expressão regular.
valor = r"R\$\s?\d+[.,]?\d*,\d{2}"
data =  r"\d{2}/\d{2}/\d{4}"
tipo = r"Tipo:\s?(.+)"
instituicao = r"Institui.{1,3}ao\s?:\s?(.+)"
nome = r"Nome:\s?(.+)"
cpf_cnpj = r"(?:CPF/CNPJ|CPF|CNPJ):\s?(.+)"

# Define uma função chamada extrair_campos_documento.
# Essa função recebe como parâmetro o texto extraído de um documento.
def extrair_campos_documento(texto):

    # Procura dentro do texto o primeiro trecho que combine com o padrão de valor em reais.
    # Se encontrar algo como "R$ 35,00", guarda o resultado na variável resultado.
    # Se não encontrar nada, resultado recebe None.
    resultado = re.search(valor, texto)
    resultado_data = re.search(data, texto)
    resultado_tipo = re.search(tipo, texto)
    resultado_instituicao = re.search(instituicao, texto)
    resultado_nome = re.search(nome, texto)
    resultado_cpf_cnpj = re.search(cpf_cnpj, texto)

    # Verifica se algum valor foi encontrado no texto.
    if resultado:

        # Pega exatamente o trecho encontrado pela expressão regular.
        # Exemplo: "R$ 35,00".
        valor_extraido = resultado.group()

    # Caso nenhum valor tenha sido encontrado.
    else:

        # Define valor_extraido como None para indicar ausência de valor.
        valor_extraido = None

    # Verifica se alguma data foi encontrado no texto.
    if resultado_data:

        data_extraida = resultado_data.group()

    # Caso nenhuma data tenha sido encontrado.
    else:

        data_extraida = None

    if resultado_tipo:

        #O group(1) pega só o que vem depois de Tipo:, por exemplo: Pix
       tipo_extraido = resultado_tipo.group(1).strip()

    else:

        tipo_extraido = None

    if resultado_instituicao:

        #O group(1) pega só o que vem depois de Instituição:, por exemplo: Instituição
       instituicao_extraida = resultado_instituicao.group(1).strip()

    else:

        instituicao_extraida = None

    if resultado_nome:

        #O group(1) pega só o que vem depois de Nome:, por exemplo: Nome
       nome_extraido = resultado_nome.group(1).strip()

    else:

        nome_extraido = None

     # Verifica se algum valor foi encontrado no texto.
    if resultado_cpf_cnpj:

        # Pega exatamente o trecho encontrado pela expressão regular.
        # Exemplo: "R$ 35,00".
        cpf_cnpj_extraido = resultado_cpf_cnpj.group(1).strip()

    # Caso nenhum valor tenha sido encontrado.
    else:

        # Define valor_extraido como None para indicar ausência de valor.
        cpf_cnpj_extraido = None

    # Cria um dicionário chamado campos.
    # Esse dicionário organiza os dados extraídos do documento.
    campos = {

        # Cria a chave "valor" e armazena nela o conteúdo da variável valor_extraido.
        "valor": valor_extraido,
        "data": data_extraida,
        "tipo": tipo_extraido,
        "instituicao": instituicao_extraida,
        "nome": nome_extraido,
        "cpf_cnpj": cpf_cnpj_extraido,
    }

    # Retorna o dicionário com os campos extraídos.
    return campos