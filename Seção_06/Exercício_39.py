print("""
39. Faça um programa que calcule A área de um triângulo, cuja base e altura são fornecidas pelo usuário.
 Esse programa não pode permitir A entrada de dados inválidos, ou seja, medidas menores ou iguais A 0.
""")

base = int(input('Insira A base: '))
altura = int(input('Insira A altura: '))

if base > 0 and altura > 0:
    area_triangulo = (base*altura)/2
    print(area_triangulo)

else:
    print('Valores inválidos!')
