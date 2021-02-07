print("""
8. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
""")

menor = maior = 0
for num in range(10):
    numero = int(input(f'Insira o {num + 1} número: '))
    if num == 0:
        menor = maior = numero
    else:
        if numero >= maior:
            maior = numero
        if numero <= menor:
            menor = numero

print(f'\n O maior número digitado foi {maior} e o menor {menor}.')
