print("""
53. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triangulo de Floyd. Para n = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
""")

variavel = 0
numero = int(input('Quantas linhas: '))
for num in range(1, numero + 1):
    for x in range(num, num * 2):
        variavel += 1
        print(variavel, end=' ')
    print('')
