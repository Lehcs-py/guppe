print("""
7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima A mensagem "Números iguais".
""")

print('Mostra qua número é maior.')
num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))

if num1 > num2:
    print(f'{num1} é maior.')
elif num1 < num2:
    print(f'{num2} é maior.')
else:
    print('Números iguais.')
