print("""
26. Faca um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
""")

contador11 = contador13 = contador17 = 0
num = int(input('Insira o número: '))
while True:
    num += 1

    if num % 11 == 0 and contador11 < 1:
        print(f'11: {num}')
        contador11 += 1

    elif num % 13 == 0 and contador13 < 1:
        print(f'13: {num}')
        contador13 += 1

    elif num % 17 == 0 and contador17 < 1:
        print(f'17: {num}')
        contador17 += 1

    elif contador11 > 1 and contador13 > 1 and contador17 > 1:
        break

    else:
        pass
