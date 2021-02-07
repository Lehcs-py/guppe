print("""
55. Escreva um programa que leia um inteiro não negativo n e imprima A soma dos n primeiros números primos.
""")

numero = int((input('Insira o número: ')))

soma = 0
for num in range(1, numero + 1):
    if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num != 1) or (num in (2, 3, 5, 7)):
        soma += num

    else:
        pass

print(f'Soma = {soma}')
