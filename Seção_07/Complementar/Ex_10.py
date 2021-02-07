print("""
10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro matriz de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
# Exemplos:
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19 20
""")

vetor10_1 = str(input('Insira o 1° matriz com 10 elementos: ')).split()
vetor10_2 = str(input('Insira o 2° matriz com 10 elementos: ')).split()
vetor20 = list()

for num in range(10):
    vetor20.append(vetor10_1[num])
    vetor20.append(vetor10_2[num])

print(vetor20)


