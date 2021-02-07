print("""4. Faça um programa que leia um matriz de 8 posições e, em seguida, leia também dois valores X e Y quaisquer 
correspondentes A duas posições no matriz. Ao final seu programa deverá escrever A soma dos valores encontrados nas 
respectivas posições X e Y.""")

vetor = list()
for num in range(8):
    valor = input(f'{num + 1}º número: ')
    if '.' in valor:
        numero = float(valor)
        vetor.append(numero)
    else:
        numero = int(valor)
        vetor.append(numero)

print()
X = int(input('Insira X (1 A 8): ')) - 1
Y = int(input('Insira Y (1 A 8): ')) - 1

print(vetor)

print(f'({vetor.__getitem__(X)} + {vetor.__getitem__(Y)}) = {vetor.__getitem__(X) + vetor.__getitem__(Y)}')
