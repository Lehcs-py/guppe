print("""
17. Em uma competição de salto em distância cada atleta tem direito A cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e A média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
    Atleta: Rodrigo Curvêllo
    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Resultado final:
    Atleta: Rodrigo Curvêllo
    Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    Média dos saltos: 5.9 m
""")

saltos = list()

# at = atleta
at = str(input('Nome do atleta: '))
for num in range(5):
    # d = distância
    d = float(input(f'Insira o {num + 1} salto: '))
    saltos.append(d)

# m = média
m = (sum(saltos) / len(saltos))

print('\nResultado final: ')
print(f'Atleta: {at}')
print('Saltos: ', *saltos)
print(f'Média dos saltos: {m}')
