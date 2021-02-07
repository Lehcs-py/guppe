print("""
10. Faça um programa que calcule e mostre A soma dos 50 primeiros números pares.
""")

contador = num = soma = 0
while contador != 50:
    num += 1
    if num % 2 == 0:
        soma += num
        contador += 1
    else:
        pass

print(f'A soma dos 50 primeiros números impares é: {soma}')
