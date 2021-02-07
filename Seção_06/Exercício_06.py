print("""
6. Faça um programa que leia 10 inteiros e imprima sua média.
""")

soma = 0
for num in range(10):
    numero = int(input(f'Insira o {num + 1}: '))
    soma += numero

media = soma/10
print(f'A média dos 10 número é: {media}.')
