print("""
30. Leia um valor em Real e A cotação do Dólar. Em seguida, imprima o valor correspondente em dólares.
""")

real = float(input('Insira o valor em Real para A conversão em Dólar: '))
c_dolar = float(input('Insira o valor da cotação do Dólar: '))
conversao = real / c_dolar
print(f'R$ {real} = US$ {conversao}.')
