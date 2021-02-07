print("""
3. Leia um número real. Se o número for positivo imprima A raiz quadrada. Do contrário, imprima o número ao quadrado.
""")

num = float(input('Insira um número real, positivo = √x, negativo = x².: '))
if num >= 0:
    raiz = num ** 0.5
    print(f'O número é positivo, portanto, sua raiz quadrada é {raiz}.')
else:
    quadrado = num ** 2
    print(f'O número é negativo, portanto, o seu quadrado é {quadrado}.')
