print("""
37. Considere um matriz A com 11 elementos onde A1 < A2 < ...< A6 > A7 > A8 > ...> Al1, ou seja, está ordenado em ordem crescente até o sexto elemento,
e A partir desse elemento está ordenado em ordem decrescente. Dado o matriz da questão anterior, proponha um algoritmo para ordenar os elementos.
""")

# matriz = list()
# for contador in range(11):
#     matriz.append(int(input(f'Insira {contador + 1}º número: ')))

vetor = [96, 35, 10, 77, 48, 17, 19, 20, 55, 60, 30]
v1 = vetor[:6]
v1.sort()
v2 = vetor[6::]
v2.sort(reverse=True)

v3 = v1 + v2

print(v3)
