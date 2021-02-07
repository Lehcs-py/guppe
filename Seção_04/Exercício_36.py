print("""
36. Leia A Altura e o Raio de um cilindro circular e imprima o Volume do cilindro.
    O volume de um cilindro circular é calculado por meio da seguinte
    fórmula: V = pi*raio²*altura, onde pi = 3.141592 .
""")

altura = float(input('Altura do cilindro: '))
raio = float(input('Raio do circulo do cilindro: '))
pi = 3.141592
volume = (pi * (raio ** 2) * altura)
print(f'O volume desse cilindro é aproximadamente: {volume}')
