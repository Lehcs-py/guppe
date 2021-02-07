print("""
25. Faça um programa que preencha um matriz de tamanho 100 com os 100 primeiros naturais que não são múltiplos de 7 ou que terminam com 7.
""")

c = 0  # c = contador
vetorsem7 = list()
while len(vetorsem7) < 100:
    c += 1
    if c % 7 == 0 or str(c)[::-1][0] == '7':
        pass
    else:
        vetorsem7.append(c)

print(vetorsem7)
