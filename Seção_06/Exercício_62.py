print("""
62. Se os números de 1 A 5 são escritos em palavras: um, dois, três, quatro, cinco, então há 2 + 4 + 4 + 6 + 5 = 21 letras usadas no total.
Faça um programa que conte quantas letras seriam utilizadas se todos os números de 1 A 1000 (mil) fossem escritos em palavras.
OBS: Não conte espaços ou hifens.
""")

soma = 0
for num in range(1, 1001):
    str_num = str(num)

    for indice, algarismo in enumerate(str_num):
        if algarismo == '1':
            soma += 2
        if algarismo == '2' or algarismo == '3' or algarismo == '6' or algarismo == '7' or algarismo == '8' or algarismo == '9' or algarismo == '0':
            soma += 4
        if algarismo == '4':
            soma += 6
        if algarismo == '5':
            soma += 5
        else:
            pass

print(f'Soma = {soma}')
