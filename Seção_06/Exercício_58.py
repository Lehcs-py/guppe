print("""
58. Faça um programa que some os números primos existentes entre A e B, onde A e B são números informados pelo usuário.
""")

a, b = int(input('Insira A: ')), int(input('Insira B: '))
if a < b:
    pass
else:
    c = a
    a = b
    b = c

soma = 0
for num in range(a, b + 1):
    if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num != 1) or (num in (2, 3, 5, 7)):
        soma += num
    else:
        pass

print(f'A soma dos primos entre o intervalo [{a}, {b}] é {soma}.')
