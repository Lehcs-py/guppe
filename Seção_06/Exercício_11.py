print("""
11. Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente.
""")

numero = int(input('Insira o número: '))
for num in range(0, numero + 1):
    print(num)
