print("""
31. Faça um programa que receba A altura e o peso de uma pessoa.
De acordo com A tabela A seguir, verifique e mostre qual é A classificação dessa pessoa:

                 Altura           Até 60       Entre 60 e 90 (inclusive)     Acima de 90
    Menor que 1.20         A                            D                                                G
    De 1.20 A 1.70           B                            E                                                H
    Maior que 1.70         C                            F                                                 I
""")

altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))

clas = str
if altura < 1.20:
    if peso <= 60:
        clas = 'A'

    elif 60 < peso <= 90:
        clas = 'D'

    else:
        clas = 'G'

elif 1.20 <= altura <= 1.70:
    if peso <= 60:
        clas = 'B'

    elif 60 < peso <= 90:
        clas = 'E'

    else:
        clas = 'H'

elif altura > 1.70:
    if peso <= 60:
        clas = 'C'

    elif 60 < peso <= 90:
        clas = 'F'

    else:
        clas = 'I'

else:
    print('Tem algo de errado!')

print(f'Sua classificação é {clas}.')
