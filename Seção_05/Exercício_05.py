print("""
5. Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
""")

num = int(input('Insira um número para verificar se é impar ou par: '))
if (num % 2) == 0:
    print(f'{num} é um número par.')

else:
    print(f'{num} é um número impar.')
