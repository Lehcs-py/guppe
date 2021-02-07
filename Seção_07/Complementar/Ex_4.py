print("""
4. Faça um Programa que leia um matriz de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
""")

escolha = int(input('Qual forma? 1 ou 2: '))
print('\n')

if escolha == 1:
    # Primeira forma:
    vetor10 = str(input('Insira um matriz de 10 caracteres: ')).split()
    consoantes = list()
    contador = 0

    for indice, letra in enumerate(vetor10):
        if letra in ['B', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']:
            contador += 1
            consoantes.append(letra)

        else:
            pass

    print(f'\nNesse matriz foram encontradas {contador} consoantes são elas:')
    for indice, consoante in enumerate(consoantes):
        print(consoante, end=' ')


elif escolha == 2:
    # Segunda forma:
    vetor10 = list()
    for num in range(10):
        letra = str(input(f'Insira a {num + 1}° letra: '))
        vetor10.append(letra)
    consoantes = list()
    contador = 0

    for indice, letra in enumerate(vetor10):
        if letra in ['B', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']:
            contador += 1
            consoantes.append(letra)

        else:
            pass

    print(f'\nNesse matriz foram encontradas {contador} consoantes são elas:')
    for indice, consoante in enumerate(consoantes):
        print(consoante, end=' ')

else:
    print('Essa forma não existe.')
