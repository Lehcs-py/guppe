print("""
15. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem crescente.
""")

numero = int(input('Insira o número: '))
for num in range(1, numero + 1):
    if num % 2 == 1:
        print(num)
    else:
        pass
