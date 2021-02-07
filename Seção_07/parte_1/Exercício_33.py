print("""
33. Faça um programa que leia um matriz de 15 posições e o compacte, ou seja, elimine as posições com valor zero. Para isso, todos os elementos à
frente do valor zero, devem ser movidos uma posição para trás no matriz.
""")

vetor = list()
for contador in range(15):
    vetor.append(int(input(f'Insira {contador + 1}º número: ')))

if vetor.__contains__(0):
    for num in range(vetor.count(0)):
        vetor.remove(0)

print(vetor)
