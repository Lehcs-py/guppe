print("""
2. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule A raiz quadrada do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
""")

num = int(input('Insira um número para obter sua raiz quadrada: '))
if num >= 0:
    print(f'√{num} = {num**0.5}')

else:
    print('O número inserido é inválido!')
