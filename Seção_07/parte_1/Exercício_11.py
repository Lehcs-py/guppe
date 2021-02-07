print("""
11. Faça um programa que preencha um matriz com 10 números reais, calcule e mostre
A quantidade de números negativos e A soma dos números positivos desse matriz.
""")

# matriz = list()
# for contador in range(10):
#     matriz.append(float(input(f'Insira {contador + 1}º número: ')))

vetor = [74, 67, -18, -33, -57, 76, 59, 78, 72, -66]
c_n = 0  # c_n = contador_negativo
soma = 0
for numero in vetor:
    if numero < 0:
        c_n += 1
    if numero > 0:
        soma += numero
        pass

print(f'Numeros negativos: {c_n}')
print(f'Soma: {soma}')
