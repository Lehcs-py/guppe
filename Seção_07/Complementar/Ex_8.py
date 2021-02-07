print("""
8. Faça um Programa que peça A idade e A altura de 5 pessoas, armazene cada informação no seu respectivo matriz.
Imprima A idade e A altura na ordem inversa A ordem lida.
""")

idades = list()
alturas = list()
for num in range(5):
    print(f'{num + 1}° pessoa: ')
    idade = int(input(f'Insira A idade: '))
    idades.append(idade)

    altura = int(input(f'Insira A altura: '))
    alturas.append(altura)

    print()

for indice in range(4, -1, -1):
    print(f'Pessoa {indice + 1}, Idade: {idades[indice]}, Altura: {alturas[indice]}')

