print("""
17. Leia um matriz de 10 posições e atribua valor para todos os elementos que possuirem valores negativos
""")

# matriz = list()
# for contador in range(10):
#     matriz.append(float(input(f'Insira {contador + 1}º número: ')))

vetor = [70, 44, -17, 64, 1, 64, -15, 77, -36, 7]
for num in vetor:
    if num < 0:
        vetor.__setitem__(vetor.index(num), 0)

print(f'Vetor: {vetor}')
