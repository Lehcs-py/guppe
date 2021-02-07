print("""
6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como A diferença existente entre ambos.
""")

print('Para obter o maior...')
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

if num1 > num2:
    print(f'{num1} > {num2}')
elif num2 > num1:
    print(f'{num2} > {num1}')
else:
    print(f'{num1} = {num2}')
