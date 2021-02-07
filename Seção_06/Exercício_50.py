print("""
50. Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano.
Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.
""")

chico = 150
ze = 110
contador = 0

while True:
    chico += 2
    ze += 3
    contador += 1

    if chico >= ze:
        pass
    else:
        print(contador)

        print(f'{ze / 100} > {chico / 100}')

        break
