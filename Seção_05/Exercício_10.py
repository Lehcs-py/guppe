print("""
10. Faça um programa que receba A altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas (onde h corresponde à altura):
    Homens: (72.7*h) - 58
    Mulheres: (62.1*h) - 44.7
""")

altura = float(input('Insira sua altura: '))
sexo = input('Insira seu sexo: ').upper().strip()

if sexo[0] == 'M' or sexo[0] == 'H':
    print(f'Seu peso ideal é de {(72.7 * altura) - 58} kg.')

elif sexo[0] == 'F' or sexo[0:2] == 'MU':
    print(f'Seu peso ideal {(62.1 * altura) - 44.7}.')

else:
    print('Tem algo errado aí...')
