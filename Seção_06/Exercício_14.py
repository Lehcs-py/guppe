print("""
14. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente.
""")

numero = int(input('Insira o número: '))
for num in range(numero + 1, -1, -1):
    if num % 2 == 0:
        print(num)
    else:
        pass
