print("""
9. Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.
""")

valores_pares = list()
contador = 0
while len(valores_pares) != 6:
    contador += 1
    valor_par = int(input(f'Insira o {contador}º valor par: '))
    while valor_par % 2 != 0:
        valor_par = int(input(f'Insira o {contador}º valor par: '))

    valores_pares.append(valor_par)

print('\nInverso: ')
print(*reversed(valores_pares))
