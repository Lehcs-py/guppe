print("""
41. Faça um programa que calcula A associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado.
O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para resistência igual A zero.
    R = (R1 * R2)/(R1 + R2)
""")

while True:
    print('\n')
    R1 = int(input('Insira R1: '))
    R2 = int(input('Insira R2: '))
    resistencia = (R1 * R2)/(R1 + R2)

    print(f'R = {resistencia}')

    if resistencia == 0:
        break
    else:
        pass
