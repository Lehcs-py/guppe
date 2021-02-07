print("""
9. Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.
""")

numero = int(input('Insira o número: '))
for num in range(0, numero + 1):
    if num % 2 != 0:
        print(num)
    else:
        pass
