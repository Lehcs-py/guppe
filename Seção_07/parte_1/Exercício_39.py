def pascal(numero):
    from math import factorial
    variavel1 = 0
    for num in range(1, numero + 1):
        variavel2 = -1

        for x in range(1, num + 1):
            variavel2 += 1
            try:
                calculo = (factorial(variavel1) / (factorial(variavel2) * factorial(variavel1 - variavel2)))
            except:
                calculo = 1

            print(f'{calculo:.0f}', end=' ')

        print('')
        variavel1 += 1


pascal(int(input('Insira o número de linhas: ')))
