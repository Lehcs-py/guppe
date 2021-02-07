print("""
32. Leia um número inteiro e imprima A soma do sucessor do seu triplo com o antecessor de seu dobro.
""")

num = int(input('Insira um número inteiro, para obter A soma do sucessor do seu triplo com o antecessor de seu dobro: '))
soma = ((num * 3) + 1) + ((num * 2) - 1)
print(f'{(num * 3) + 1} + {((num * 2) - 1)} = {soma}')
