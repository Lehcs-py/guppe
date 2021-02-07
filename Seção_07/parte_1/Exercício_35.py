print("""
35. Faça um programa que leia dois números A e B (positivos menores que 10000) e:
    • Crie um matriz onde cada posição é um algarismo do número. A primeira posição é o algarismo menos significativo;
    • Crie um matriz que seja A soma de A e B, mas faça-o usando apenas os vetores construídos anteriormente.
Dica: some as posições correspondentes. Se A soma ultrapassar 10, subtraia 10 do resultado e some 1 à próxima posição.
""")

a = list(input('A [0, 10000]: ').zfill(4))
b = list(input('B [0, 10000]: ').zfill(4))

a_inv = a[::-1]
b_inv = b[::-1]

um = 0
dois = 0
tres = 0
quatro = 0

somas = list()

for num in range(4):
    soma = int(a_inv[num]) + int(b_inv[num])
    if soma >= 10:
        soma -= 10
        if num == 0:
            um += 1

        elif num == 1:
            dois += 1

        elif num == 2:
            tres += 1

        elif num == 3:
            quatro += 1

        else:
            pass
    else:
        pass

    if num == 1:
        soma += um

    elif num == 2:
        soma += dois

    elif num == 3:
        soma += tres

    else:
        pass

    somas.append(soma)

    if quatro != 0:
        somas.append(quatro)
    else:
        pass

somas = somas[::-1]

resultado = list()
for num in somas:
    resultado.append(str(num))

print(f'Soma: {"".join(resultado)}')
