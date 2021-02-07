print("""
Escreva o menu de opções abaixo. Leia A opção do usuário e execute A operação escolhida.
Escreva uma mensagem de erro se A opção for inválida.
    Escolha A opção:
    1- Soma de 2 números.
    2- Diferença entre números (maior pela menor).
    3- Produto entre 2 números.
    4- Divisão entre 2 números (o denominador não pode ser zero).
""")

print('''	
Escolha A opção:
1- Soma de 2 números.
2- Diferença entre números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).
''')
escolha = int(input('Escolha: '))
num1 = float(input('Um número: '))
num2 = float(input('Outro número: '))

if escolha == 1:
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado}')

elif escolha == 2:
    if num1 > num2:
        resultado = num1 - num2
        print(f'{num1} - {num2} = {resultado}')

    else:
        resultado = num2 - num1
        print(f'{num2} - {num1} = {resultado}')

elif escolha == 3:
    resultado = num1 * num2
    print(f'{num1} * {num2} = {resultado}')

elif escolha == 4:
    if num1 > num2:
        if num2 != 0:
            resultado = num1 / num2
            print(f'{num1} / {num2} = {resultado}')

    else:
        if num1 != 0:
            resultado = num2 / num1
            print(f'{num2} / {num1} = {resultado}')
