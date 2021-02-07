print("""
59. Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh, e para cada habitante entre com os seguintes
dados: consumo do mês e o código do consumidor (1-Residencial, 2-Comercial, 3-Industrial). No final imprima o maior, o menor e A média do consumo
dos habitantes; e por fim o total do consumo de cada categoria de consumidor.
""")

habitantes = int(input('Insira A quantidade de habitantes na cidade: '))

residencial = comercial = industrial =\
    total = menor = maior = kwh = contador = 0
for num in range(1, habitantes + 1):
    print("""
    Residencial [1]
    Comercial   [2]
    Industrial  [3]
    """)

    escolha = int(input('Escolha: '))
    kwh = int(input('Insira o consumo em kwh: '))

    if num == 1:
        maior = menor = kwh

    else:
        if kwh >= maior:
            maior = kwh

        elif kwh <= menor:
            menor = kwh

    if escolha == 1:
        residencial += kwh

    elif escolha == 2:
        comercial += kwh

    elif escolha == 3:
        industrial += kwh

    else:
        pass

    total += kwh
    contador = num

print(f"""
Maior consumo: {maior}
Menor consumo: {menor}
Média de consumo por habitantes: {total / contador}
Consumo total: {total}
""")
