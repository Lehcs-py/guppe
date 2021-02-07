print("""
11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
# Exemplos:
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30
""")

vetor10_1 = str(input('Insira o 1° matriz com 10 elementos: ')).split()
vetor10_2 = str(input('Insira o 2° matriz com 10 elementos: ')).split()
vetor10_3 = str(input('Insira o 3° matriz com 10 elementos: ')).split()
vetor20 = list()

for num in range(10):
    vetor20.append(vetor10_1[num])
    vetor20.append(vetor10_2[num])
    vetor20.append(vetor10_3[num])

print(vetor20)
