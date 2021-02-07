print("""
24. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando A sua altura em metros.
Encontre o aluno mais baixo e o mais alto. Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.
""")

numeros = list()
alturas = list()

for num in range(10):
    numeros.append(int(input('Número: ')))
    alturas.append(float(input('Altura: ')))
    print()

print()
print(f'Maior:\n{numeros.__getitem__(alturas.index(max(alturas)))}: {max(alturas)}')
print(f'Menor:\n{numeros.__getitem__(alturas.index(min(alturas)))}: {min(alturas)}')

