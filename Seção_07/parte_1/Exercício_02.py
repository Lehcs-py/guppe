print("""
2. Crie um programa que leia 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
""")

lista = list()

for num in range(6):
    valor = int(input(f'Insira o {num + 1}° valor: '))
    lista.append(valor)

print('Valores lidos:\n', *lista)
