import csv

def ler_csv(nome_file: str) -> list[dict]:
    """
    funcao que le csv e retorna uma lista de dicionarios
    """
    with open(nome_file, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        dados = [linha for linha in leitor_csv]
    return dados


def calcular_vendas_categoria(lista: list[dict]) -> dict:
    """
    funcao que soma a quantidade vendida por categoria
    """
    
    resultado = {}

    for linha in lista:
        if linha['Categoria'] not in resultado:
            resultado[linha['Categoria']] = linha['Quantidade']
        else:
            resultado[linha['Categoria']] += linha['Quantidade']

    return resultado
