print("""
33. Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
Exemplo: Para n = 6, i = 2 ej = 3 A saída deverá ser: 0, 2, 3, 4, 6, 8.
""")

numero = int(input('Insira A quantidade de números: '))
i = int(input('Insira i: '))
j = int(input('Insira j: '))

contador = num = 0
while contador != numero:
    if num % i == 0 and not num % j == 0:
        print(num)
        contador += 1

    elif num % j == 0 and not num % i == 0:
        print(num)
        contador += 1

    elif num % i == 0 and num % j == 0:
        print(num)
        contador += 1

    else:
        pass

    num += 1
