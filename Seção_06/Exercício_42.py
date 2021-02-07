print("""
42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores lidos, o quadrado, 
o cubo e A raiz quadrada. Finalize A entrada de dados com um valor negativo ou zero.
""")

numero = 1
while numero > 0:
    numero = int(input('Insira o número (0 para): '))

    print(f'{numero}² = {numero ** 2}'
          f'\n{numero}³ = {numero ** 3}'
          f'\n√{numero} = {numero ** 0.5}\n')
