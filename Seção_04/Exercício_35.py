print("""
35. Sejam A e B os catetos de um triângulo, onde A hipotenusa é obtida pela equação: hipotenusa = √(A²+B²).
Faça um programa que receba os valores de A e B e calcule o valor da hipotenusa através da equação.
Imprima o resultado dessa operação.
""")

a = float(input('Insira o valor do cateto A: '))
b = float(input('Insira o valor do cateto B: '))
hipotenusa = ((a ** 2) + ((b ** 2) ** 0.5))
print(f'O valor da hipotenusa é: {hipotenusa}')
print(f'√({(a ** 2)} + {(b ** 2)}) = {hipotenusa}')
