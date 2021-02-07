print("""
1. Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
""")

matriz = [[20, 16, 20, 25], [7, 20, 20, 21], [4, 19, 17, 14], [16, 23, 8, 0]]

c_10 = 0  # Contador de 10
for linha in matriz:
    for num in linha:
        if num > 10:
            c_10 += 1
        else:
            pass
print(f'Foram encontrado {c_10} números maiores que 10.')
