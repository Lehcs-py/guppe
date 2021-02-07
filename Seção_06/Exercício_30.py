print("""
30. Faça programas para calcular as seguintes sequências:
    1 + 2 + 3 + 4 + 5 + ... + n
    1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
    1 + 3 + 5 + 7 + ... + (2n - 1)
""")

numero = int(input('Insira o número (n): '))

soma1 = soma2 = soma3 = 0

for num in range(1, numero + 1):
    soma1 += num

for num in range(1, (numero*2 - 1) + 1):
    if num % 2 == 0:
        soma2 -= num
    else:
        soma2 += num

for num in range(1, (numero*2 - 1) + 1):
    if num % 2 == 0:
        pass
    else:
        soma3 += num

print(f'''    
    1 + 2 + 3 + 4 + 5 + ... + n: {soma1}
    
    1 - 2 + 3 - 4 + 5 + ... + (2n - 1): {soma2}
    
    1 + 3 + 5 + 7 + ... + (2n - 1): {soma3}
    ''')
