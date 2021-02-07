print("""
45. Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa.
Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa.
O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado quando A opção de finalizar for escolhida.
""")

escolha = ''
while escolha != 0:
    print("""
    [1] Km/h para m/s;
    [2] m/s para Km/h;
    [0] Sair.
    """)
    escolha = float(input('Escolha: '))

    if escolha == 0:
        break

    elif escolha == 1:
        kmh = float(input('Insira Km/h: '))

        ms = kmh / 3.6

        print(f'{kmh}Km/h = {ms}m/s')

    elif escolha == 2:
        ms = float(input('Insira o m/s: '))

        kmh = ms * 3.6

        print(f'{ms}m/s = {kmh}Km/h')

    else:
        pass
