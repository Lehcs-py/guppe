print("""
17. Faça um programa que calcule e mostre A área de um trapézio. Sabendo que:
A = ((base_maior + base_menor) * altura)/2 Lembre-se A base maior e A base menor devem ser números maiores que zero.
""")

print('Sobre o trapézio: ')
base_maior = float(input('  Insira o valor da base maior: '))
base_menor = float(input('  Insira o valor da base menor: '))
altura = float(input('  Insira o valor da altura: '))

if base_maior < 0 or base_menor < 0:
    print('Um ou mais valores inválidos.')

else:
    area = ((base_maior + base_menor) * altura)/2
    print(f'A area desse trapézio é igual A {area}.')