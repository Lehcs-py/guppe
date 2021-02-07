print("""
6. Faça um programa que receba do usuario um matriz com 10 posições.
Em seguida deverá ser impresso o maior e o menor elemento do matriz.
""")

vetor_ini = input('Insira o matriz: ').split()
vetor_fin = list()
contador_par = 0

for numero in vetor_ini:
    valor = int(numero)
    vetor_fin.append(valor)

print(f'Em {vetor_fin}:')
print(f'Maior valor: {max(vetor_fin)}.\nMenor valor: {min(vetor_fin)}')
