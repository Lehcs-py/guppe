print("""
37. Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem A propriedade seguinte: A soma dos dois dígitos de mais baixa ordem com os
dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio numero. Por exemplo, para o inteiro 3025, temos que:
    30 + 25 = 55
    55² = 3025
""")

for num in range(1000, 10000):
    numero = str(num)
    soma = int(numero[0:2]) + int(numero[2:5])

    if num == (soma**2):
        print(num)

    else:
        pass
