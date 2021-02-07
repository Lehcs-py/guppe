print("""
16. Utilize uma lista para resolver o problema A seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana
mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por
cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos
seguintes intervalos de valores:
    $200 - $299
    $300 - $399
    $400 - $499
    $500 - $599
    $600 - $699
    $700 - $799
    $800 - $899
    $900 - $999
    $1000 em diante
    Desafio: Crie uma fórmula para chegar na posição da lista A partir do salário, sem fazer vários ifs aninhados.
""")

salarios = list()
vendedores = int(input('Quantos vendedores trabalham nessa empresa?: '))
contador = 0
categoria_vendedor = list()
while True:
    contador += 1
    if contador <= vendedores:
        venda = int(input(f'{contador}. Valor total das vendas desse vendedor na semana: '))
        salarios.append(round((venda / 100) * 9) + 200)
    else:
        break

categorias = [(200, 299), (300, 399), (400, 499), (500, 599), (600, 699), (700, 799), (800, 899), (900, 999)]
dicionario = {(200, 299): 0, (300, 399): 1, (400, 499): 2, (500, 599): 3, (600, 699): 4, (700, 799): 5, (800, 899): 6, (900, 999): 7}
for indice, vendedor in enumerate(salarios):
    for ind, categoria in enumerate(categorias):
        if categoria[0] <= vendedor <= categoria[1]:
            categoria_vendedor.append(dicionario[categoria])
        elif 1000 < vendedor:
            categoria_vendedor.append(8)

print(f"""
    $200 - $299: {categoria_vendedor.count(0)}
    $300 - $399: {categoria_vendedor.count(1)}
    $400 - $499: {categoria_vendedor.count(2)}
    $500 - $599: {categoria_vendedor.count(3)}
    $600 - $699: {categoria_vendedor.count(4)}
    $700 - $799: {categoria_vendedor.count(5)}
    $800 - $899: {categoria_vendedor.count(6)}
    $900 - $999: {categoria_vendedor.count(7)}
    $1000 em diante: {categoria_vendedor.count(8)} 
""")
