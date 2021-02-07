print("""
4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    O número digitado ao quadrado.
    A raiz quadrada do número digitado.
""")

num = float(input('Insira um número real, caso positivo retorno seu quadrado e sua raiz.: '))

if num >= 0:
    print(f'{num}² = {num**2}\n√{num} = {num**0.5}.')
