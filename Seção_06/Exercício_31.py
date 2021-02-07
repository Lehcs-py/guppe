print("""
31. Faça um programa que calcule e escreva o valor de S
    S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
""")

variante = soma = 0
for num in range(1, 100):
    if num % 2 == 0:
        pass

    else:
        variante += 1
        soma += num/variante

print(f'1/1 + 3/2 + 5/3 + 7/4 ... 99/50: {soma}')
