print("""
14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para A vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para A vítima?"
    "Já trabalhou com A vítima?"
    O programa deve no final emitir uma classificação sobre A participação da pessoa no crime. Se A pessoa responder positivamente A 2 questões ela
    deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
""")

perguntas = [
    input("Telefonou para A vítima?: "), input("Esteve no local do crime?: "), input("Mora perto da vítima?: "),
    input("Devia para A vítima?: "), input("Já trabalhou com A vítima?: ")
]

contador = 0
for indice, resposta in enumerate(perguntas):
    resp = resposta[0]

    if resp == 's':
        contador += 1
    else:
        pass

print('\nClassificação: ')
if 0 < contador < 2:
    print('Inocente.')
elif contador == 2:
    print('Suspeito.')
elif 2 < contador <= 4:
    print('Cúmplice.')
elif contador == 5:
    print('Assassino.')
else:
    print('OXE')
