print("""
34. Leia o valor do Raio de um círculo e calcule e imprima A Área do circulo correspondente.
A área do circulo é pi * raio², considere pi = 3.141592 .
""")

raio = float(input('Insira o valor do Raio do circulo para obter sua Área: '))
pi = 3.141592
area = pi * (raio ** 2)
print(f'A área desse circulo é igual A {area}.')
