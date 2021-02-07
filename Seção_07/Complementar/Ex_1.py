print("""
1. Faça um Programa que leia um matriz de 5 números inteiros e mostre-os.
""")


escolha = int(input('Qual forma? 1 ou 2: '))
print('\n')

if escolha == 1:
    # Primeira forma:
    vetor5 = str(input('Insira 5 um matriz números: ')).split()

    print(*vetor5)

elif escolha == 2:
    # Segunda forma:
    vetor5 = list()
    for num in range(5):
        numero = int(input(f'Insira o {num + 1}° número: '))
        vetor5.append(numero)

    print(*vetor5)

else:
    print('Essa forma não existe.')
