print("""
24. Leia um valor de área em Metros Quadrados m² e apresente-o convertido em Acres.
A fórmula de conversão é: A = M * 0.000247, sendo M A área em metros quadrados e A A ára em acres.
""")

metro_quadrado = float(input('Insira o valor da área em Metros Quadrados pra A conversão em Acres: '))
acre = metro_quadrado * 0.000247
print(f'{metro_quadrado} m² = {acre} ac.')
