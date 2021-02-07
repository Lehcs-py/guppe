print("""
12. Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente.
""")

numero = int(input('Insira o número: '))
for num in range(numero, -1, -1):
    print(num)
