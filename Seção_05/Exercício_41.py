print("""
41. Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com A tabela abaixo:

       IMC            Classificação
     < 18.5       |  Abaixo do Peso
    18.6 - 24.9   |  Saudável
    25.0 - 29.9   |  Peso em excesso
    30.0 - 34.9   |  Obesidade grau I
    35.0 - 39.9   |  Obesidade grau II
    >= 40.0       |  Obesidade grau III
""")

peso = int(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura ** 2)

print(f"\n IMC: {imc:.1f} \n")

if imc < 18.5:
    print('Abaixo do peso.')

elif 18.5 <= imc < 25:
    print('Saudável.')

elif 25 <= imc < 30:
    print('Peso em excesso.')

elif 30 <= imc < 35:
    print('Obesidade de grau I.')

elif 35 <= imc < 40:
    print('Obesidade de grau II.')

elif 40 <= imc:
    print('Obesidade de grau III.')
