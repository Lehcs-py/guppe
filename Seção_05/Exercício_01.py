print("""
1. Faça um programa que receba dois números e mostre qual deles é o maior:
""")

print('Qual número é o maior.')
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

if num1 > num2:
    print(f'Entre {num1} e {num2} o maior é {num1}.')

elif num2 > num1:
    print(f'Entre {num1} e {num2} o maior é {num2}.')
