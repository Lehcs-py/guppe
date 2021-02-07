print("""
1. Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.
""")

contador = num = 0
while contador != 6:
    if num % 3 == 0:
        print(num)
        contador += 1
    else:
        pass
    num += 1
