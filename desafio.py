from etl import ler_csv, calcular_vendas_categoria

path_file = 'vendas.csv'

print(calcular_vendas_categoria(ler_csv(path_file)))