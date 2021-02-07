print("""
14. Faça um programa que leia um matriz de 10 posições e verifique se existem valores iguais e os escreva na tela.
""")

# matriz = list()
# for contador in range(10):
#     matriz.append(int(input(f'Insira {contador + 1}º número: ')))

repetido = list()
vetor = [100, 82, 10, 55, 8, 55, 96, 100, 1, 15]
for num in vetor:
    if vetor.count(num) > 1:
        repetido.append(num)
    else:
        pass
    repetido = list(set(repetido))

print('Valores repetidos:\n', *repetido)
