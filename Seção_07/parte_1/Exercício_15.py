print("""
15. Leia um matriz com 20 numeros inteiros, Escreva os elementos do matriz eliminando elementos repetidos.
""")

# matriz = list()
# for contador in range(20):
#     matriz.append(int(input(f'Insira {contador + 1}º número: ')))

vetor = [19, 62, 50, 1, 63, 1, 8, 17, 89, 94, 24, 63, 22, 43, 22, 75, 99, 39, 44, 22]
vetor = list(set(vetor))

print(*vetor)
