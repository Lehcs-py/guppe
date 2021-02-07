print("""
28. Leia 10 números inteiros e armazene em um matriz v. Crie dois novos vetores v1 e v2. Copie os valores ímpares de v para v1, e os valores pares de v
para v2. Note que cada um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os elementos são utilizados. No final escreva os elementos
UTILIZADOS de vl e v2.
""")

# v = list()
# for contador in range(10):
#     v.append(int(input(f'Insira {contador + 1}º número: ')))

v = [1, 22, 17, 85, 62, 98, 65, 1, 43, 77]
v1 = list()
v2 = list()
for num in v:
    if num % 2 == 0:
        v2.append(num)
    else:
        v1.append(num)

print(f'V1: {v1}')
print(f'V1: {v2}')
