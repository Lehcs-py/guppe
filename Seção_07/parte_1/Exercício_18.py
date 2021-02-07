print("""
18. Faça um programa que leia um matriz de 10 numeros. Leia um número x. Conte os multiplos de um número x inteiro num matriz e mostre-os na tela.
""")

# matriz = list()
# for contador in range(10):
#     matriz.append(int(input(f'Insira {contador + 1}º número: ')))

vetor = [27, 22, 10, 1, 39, 65, 94, 70, 30, 60]
x = int(input('Insira x: '))
multiplos = list()
for num in vetor:
    if num % x == 0:
        multiplos.append(num)
    else:
        pass

print(f'Multiplo(s) de x: {multiplos}')
