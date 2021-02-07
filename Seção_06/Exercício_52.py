print("""
52. Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor
serão necessárias para atender ao saque com A menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
""")

dinheiro = int(input('Quanto quer sacar?: '))
cem = cinquenta = vinte = dez = cinco = dois = um = 0
while not dinheiro == 0:
    if dinheiro >= 100:
        dinheiro -= 100
        cem += 1

    elif 100 > dinheiro >= 50:
        dinheiro -= 50
        cinquenta += 1

    elif 50 > dinheiro >= 20:
        dinheiro -= 20
        vinte += 1

    elif 20 > dinheiro >= 10:
        dinheiro -= 10
        dez += 1

    elif 10 > dinheiro >= 5:
        dinheiro -= 5
        cinco += 5

    elif 5 > dinheiro >= 2:
        dinheiro -= 2
        dois += 1

    elif dinheiro >= 1:
        dinheiro -= 1
        um += 1

    else:
        pass

print(f'\nNotas de cem: {cem}'
      f'\nNotas de cinquenta: {cinquenta}'
      f'\nNotas de vinte: {vinte}'
      f'\nNotas de dez: {dez}'
      f'\nNotas de cinco: {cinco}'
      f'\nNotas de dois: {dois}'
      f'\nNotas de um: {um}')
