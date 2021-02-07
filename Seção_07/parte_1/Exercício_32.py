print("""
32. Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa elementos repetidos).
Calcule e mostre os vetores resultantes em cada caso abaixo:
    • Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y.
    • Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição em y.
    • Diferença entre x e y: todos os elementos de x que não existam em y.
    • Interseção entre x e y: apenas os elementos que aparecem nos dois vetores.
    • União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x.
""")

# x = list()
# print('Para X: ')
# for contador in range(5):
#     x.append(int(input(f'Insira {contador + 1}º número: ')))

# y = list()
# print('Para Y: ')
# for contador in range(5):
#     y.append(int(input(f'Insira {contador + 1}º número: ')))

x = [99, 7, 17, 99, 98]
y = [88, 7, 36, 82, 34]
soma = list()
produto = list()
diferenca = list()
interseccao = list()
uniao = list()

for num in range(5):
    soma.append(x[num] + y[num])
    produto.append(x[num] * y[num])
    diferenca.append(x[num] - y[num])

for num1 in x:
    for num2 in y:
        if num1 in uniao:
            pass

        else:
            uniao.append(num1)

for num1 in x:
    for num2 in y:
        if num1 == num2:
            if num1 in interseccao:
                pass

            else:
                interseccao.append(num1)

        else:
            pass

print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Diferença: {diferenca}')
print(f'Intersecção: {interseccao}')
print(f'União: {uniao}')
