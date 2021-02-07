print("""
30. Faça um programa que receba três números e mostre-os em ordem crescente.
""")

print('Para organizar enm ordem crescente...')
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
num3 = int(input('Insira mais um número: '))

if num1 > num2 > num3:
    print(num1, num2, num3)

elif num1 > num3 > num2:
    print(num1, num3, num2)

elif num2 > num1 > num3:
    print(num2, num1, num3)

elif num2 > num3 > num1:
    print(num2, num3, num1)

elif num3 > num2 > num1:
    print(num3, num2, num1)

elif num3 > num1 > num2:
    print(num3, num1, num2)
