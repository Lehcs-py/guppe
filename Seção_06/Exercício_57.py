print("""
57. Faça um programa que conte quantos números primos existem entre A e B, onde A e B são números informados pelo usuário.
""")

a, b = int(input('Insira A: ')), int(input('Insira B: '))
if a < b:
    pass
else:
    c = a
    a = b
    b = c

contador = 0
for num in range(a, b + 1):
    if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num != 1) or (num in (2, 3, 5, 7)):
        contador += 1
    else:
        pass

print(f'Entre o intervalo [{a}, {b}] existem {contador} numero primos.')
