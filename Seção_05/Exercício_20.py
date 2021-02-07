print("""
 20. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um
triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
    O comprimento de cada lado de um triângulo é menor do que A soma dos outros dois lados.
    Chama-se equilátero o triângulo que tem três lados iguais.
    Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
""")

valor_a = float(input('Insira o valor A: '))
valor_b = float(input('Insira o valor B: '))
valor_c = float(input('Insira o valor C: '))

if valor_a < valor_b + valor_c and valor_b < valor_a + valor_c and valor_c < valor_a + valor_b:
    if valor_a == valor_b == valor_c:
        print('Esse triângulo é Equilátero.')

    elif valor_a == valor_b != valor_c or valor_b == valor_c != valor_b or valor_a == valor_c != valor_b:
        print('Esse triângulo é Isóscele.')

    elif valor_a != valor_b != valor_c:
        print('Esse triângulo é Escaleno.')

else:
    print('Não é possível formar um triângulo com esses valores.')
