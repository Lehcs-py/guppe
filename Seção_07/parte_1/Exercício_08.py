print("""
8. Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.
""")

valores = list()
for num in range(6):
    valor = int(input(f"{num + 1}º valor: "))
    valores.append(valor)

print('\nInverso: ')
print(*reversed(valores))
