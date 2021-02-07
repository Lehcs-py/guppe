print("""
56. Faça um programa que calcule A soma de todos os números primos abaixo de dois milhões.
""")

numero = 2000000

soma = 0
for num in range(1, numero + 1):
    if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num != 1) or (num in (2, 3, 5, 7)):
        soma += num

    else:
        pass

print(f'Soma = {soma}')
