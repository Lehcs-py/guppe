print("""
47. Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
    • adição (opção 1)
    • subtração (opção 2)
    • multiplicação (opção 3)
    • divisão (opção 4).
    • saída (opção 5)
O programa deve possibilitar ao usuário A escolha da operação desejada, A exibição do resultado e A volta ao menu de opções.
O programa só termina quando for escolhida A opção de saída (opção 5).
""")

num1, num2 = int(input('1° número: ')), int(input('2° número: '))

escolha = ''
while escolha != 0:
    print("""
    Adição        (opção [1])
    Subtração     (opção [2])
    Multiplicação (opção [3])
    Divisão       (opção [4])
    Saída         (opção [5])
    """)
    escolha = float(input('Escolha: '))

    if escolha == 5:
        print('Adeus!')
        break

    elif escolha == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')

    elif escolha == 2:
        diferenca = num1 - num2
        print(f'{num1} - {num2} = {diferenca}')

    elif escolha == 3:
        multiplicacao = num1 * num2
        print(f'{num1} * {num2} = {multiplicacao}')

    elif escolha == 4:
        divisao = num1 / num2
        print(f'{num1} / {num2} = {divisao}')

    else:
        pass
