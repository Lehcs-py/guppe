print("""
18. Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza A operação, mostrando o resultado e saindo.
""")

print('''
[1] Soma
[2] Multiplicação
[3] Subtração
[4] Divisão
''')

escolha = int(input('Escolha: '))
num1 = int(input('Primeiro valor numerico para A operação: '))
num2 = int(input('Segundo valor numerico para A operação: '))

if escolha == 1:
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado}')

elif escolha == 2:
    resultado = num1 * num2
    print(f'{num1} * {num2} = {resultado}')

elif escolha == 3:
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado}')

elif escolha == 4:
    resultado = num1 / num2
    print(f'{num1} / {num2} = {resultado}')

else:
    print('Escolha inválida.')
