print("""
36. Faça um programa que calcule A diferença entre A soma dos quadrados dos primeiros 100 números naturais e o quadrado da soma.
Ex: A soma dos quadrados dos dez primeiros números naturais é,
    12 + 22 +... +102 = 385
O quadrado da soma dos dez primeiros números naturais é,
    (1 +2 + .. + 10)**2 = 552 = 3025
A diferença entre A soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025 - 385 = 2640.
""")

soma_quadrados = soma = 0
for num in range(1, 101):
    soma_quadrados += (num**2)
    soma += num

calculo = (soma**2) - soma_quadrados

print(f"A diferença entre A soma dos quadrados dos cem primeiros números naturais e o quadrado da soma é: {calculo} ")
