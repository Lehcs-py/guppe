print("""
25. Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
""")

soma = 0
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        soma += num
    else:
        pass

print(f'A soma dos numero divisiveis por 3 ou 5 abaixo de 1000 é: {soma}')
