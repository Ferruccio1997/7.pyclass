from typing import List

# def media_lista(lista: List[float]) -> float:
#     return sum(lista) / len(lista)


# def filtra_valores(lista: List[float], limite: float) -> float:
#     new_list = []
#     for numero in lista:
#         if numero > limite:
#             new_list.append(numero)
    
#     return new_list


# def contagem_valores_unicos(lista: List[int]) -> int:
#     return len(set(lista))


# def converte_celsius_fahrenheit(lista: List[int]) -> int:
#     return [temp*1.8 + 32 for temp in lista]


# def calcula_desvio_padrao(lista: List[int]) -> int:
#     variancia = sum((x - (sum(lista) / len(lista)))**2 for x in lista) / (len(lista) - 1)

#     return variancia ** 0.5


def encontra_valores_ausentes(lista: List[int]) -> int:
    completo = set(range(min(lista), max(lista) + 1))
    return list(completo - set(lista))

lista = [1,2,2,4,5]

print(encontra_valores_ausentes(lista))