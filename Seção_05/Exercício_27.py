print("""
27. Escreva um programa que, dada A idade de um nadador, classifique-o em uma das seguintes categorias:
    Infantil A: 5 A 7
    Infantil B: 8 A 10
    Juvenil  A: 11 A 13
    Juvenil  B: 14 A 17
    Sênior    : Maiores de 18 anos
""")

idade = int(input('Insira A idade: '))

if 5 <= idade <= 7:
    print('Infantil A')

elif 8 <= idade <= 10:
    print('Infantil B')

elif 11 <= idade <= 13:
    print('Juvenil A')

elif 14 <= idade <= 17:
    print('Juvenil B')

elif 18 <= idade:
    print('Sênior')

else:
    print('Ainda não pode participar.')
