print("""
48. Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos valores não ultrapassem quatro milhões.
""")

num = num1 = fibonacci = soma = 0
num2 = 1
while fibonacci < 3524578:
    fibonacci = num1 + num2
    num1 = num2
    num2 = fibonacci

    if fibonacci % 2 == 0:
        soma += fibonacci

    else:
        pass

print(f'Resultado = {soma}')
