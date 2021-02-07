print("""
7. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
""")

contador = soma = numero = 0
while contador < 10:
    numero = int(input(f'Insira o {contador + 1}° número: '))
    if numero > 0:
        soma += numero
        contador += 1
    else:
        pass

media = soma / 10

print(F'A média desses números, ignorando os negativos é: {media} .')
