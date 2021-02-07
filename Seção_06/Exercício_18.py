print("""
18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido.
 A quantidade de números A serem lidos deve ser fornecida pelo usuário.
""")

maior = menor = contador_maior = 0
for num in range(int(input('Quantos números serão lidos?: '))):
    numero = int(input('Insira o número: '))
    if num == 0:
        maior = menor = numero
    else:
        if maior <= numero:
            maior = numero
            contador_maior += 1
        elif menor >= numero:
            menor = numero

print(f'\nO menor número digitado foi: {menor}\n'
      f'O maior número digitado foi: {maior}\n'
      f'O maior num número foi lido {contador_maior} vezes.')
