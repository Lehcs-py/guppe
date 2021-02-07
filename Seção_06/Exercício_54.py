print("""
54. Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não.
""")

num = int(input('Insira o número: '))

if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num != 1) or (num in (2, 3, 5, 7)):
    print(f'{num} é um número primo.')

else:
    print('Não é um número primo.')
