print("""
44. Leia um número positivo do usuário, então, calcule e imprima A sequência Fibonacci até o primeiro número superior ao número lido.
Exemplo: se o usuário informou o número 30, A sequência A ser impressa será 0 1 1 2 3 5 8 13 21 34.
""")

numero = int(input('Insira o número: '))

num = num1 = fibonacci = 0
num2 = 1
while fibonacci < (numero + 1):
    print(fibonacci)

    if fibonacci == 1:
        print(fibonacci)
    else:
        pass

    fibonacci = num1 + num2
    num1 = num2
    num2 = fibonacci

    if fibonacci > numero:
        print(fibonacci)
    else:
        pass
