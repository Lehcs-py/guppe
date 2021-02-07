print("""
9. Faça um Programa que leia um matriz A com 10 números inteiros, calcule e mostre A soma dos quadrados dos elementos do matriz.
""")

vetor10 = list()
soma_quadrado = quadrado = 0
for num in range(10):
    numero = int(input(f'{num + 1}° Valor: '))
    vetor10.append(numero)

for indice, numero in enumerate(vetor10):
    quadrado = (numero ** 2)
    soma_quadrado += quadrado

print(f'A soma dos quadrado de', *vetor10, f': {soma_quadrado}')
