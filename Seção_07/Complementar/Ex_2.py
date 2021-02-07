print("""
2. Faça um Programa que leia um matriz de 10 números reais e mostre-os na ordem inversa.
""")

escolha = int(input('Qual forma? 1 ou 2: '))
print('\n')

if escolha == 1:
    # Primeira forma:
    vetor10 = str(input('Insira o matriz com 10 números: ')).split()
    vetor10.reverse()

    print(vetor10)

elif escolha == 2:
    # Segunda forma:
    vetor10 = list()
    for num in range(10):
        numero = int(input(f'Insira o {num + 1} número: '))
        vetor10.append(numero)
    vetor10.reverse()

    print(vetor10)

else:
    print('Essa forma não existe.')
