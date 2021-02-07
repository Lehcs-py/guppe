print("""
5. Faça um Programa que leia 20 números inteiros e armazene-os num matriz. Armazene os números pares no matriz PAR e os números IMPARES no matriz impar.
Imprima os três vetores.
""")

escolha = int(input('Qual forma? 1 ou 2: '))
print('\n')

if escolha == 1:
    # Primeira forma:
    vetor_par = list()
    vetor_impar = list()
    vetor20 = str(input('Insira um matriz de 20 números inteiros: ')).split()

    for indice, numero in enumerate(vetor20):
        if int(numero) % 2 == 0:
            vetor_par.append(numero)
        else:
            vetor_impar.append(numero)

    print(f'\nVetor: {vetor20}'
          f'\nVetor par: {vetor_par}'
          f'\nVetor impar: {vetor_impar}')

elif escolha == 2:
    # Segunda forma:
    vetor_par = list()
    vetor_impar = list()
    vetor20 = list()

    for num in range(20):
        numero = int(input(f'Insira o {num + 1} número: '))
        if numero % 2 == 0:
            vetor_par.append(numero)
        else:
            vetor_impar.append(numero)

        vetor20.append(numero)

    print(f'\nVetor: {vetor20}'
          f'\nVetor par: {vetor_par}'
          f'\nVetor impar: {vetor_impar}')

else:
    print('Essa forma não existe.')
