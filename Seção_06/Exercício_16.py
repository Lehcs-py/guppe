print("""
16. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem decrescente.
""")

numero = int(input('Insira o número: '))
for num in range(numero + 1, 0, -1):
    if num % 2 == 1:
        print(num)
    else:
        pass
