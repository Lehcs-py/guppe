print("""
23. Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar
é dado por: x1 * y1 + x2 * y2 + ... + Xn * Yn.
""")

# x = list()
# print('Para X:')
# for contador in range(5):
#     x.append(int(input(f'Insira {contador + 1}º número: ')))

# y = list()
# print('Para Y:')
# for contador in range(5):
#     y.append(int(input(f'Insira {contador + 1}º número: ')))

x = [94, 22, 78, 25, 24]
y = [62, 25, 89, 30, 7]
soma = 0
print(f'x: {x}')
print(f'y: {y}')
print('\nProduto escalar:', end=' ')
n = len(x)
for num in range(n):
    soma += (x[num] * y[num])
    if num + 1 < n:
        print(f'{x[num]} * {y[num]} + ', end='')
    elif num + 1 == n:
        print(f'{x[num]} * {y[num]} = ', end='')

print(f'{soma}')
