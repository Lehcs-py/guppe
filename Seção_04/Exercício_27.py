print("""
27. Leia um valor de área em Hectares e apresente-o convertido em Metros Quadrados m².
A fórmula de conversão é: M = H * 10000, sendo M A área em metros quadrados e H A área em hectares.
""")

hectare = float(input('Insira o valor da área em Hectares para A conversão em Metros Quadrados: '))
metro_quadrado = hectare * 10000
print(f'{hectare} ha = {metro_quadrado} m².')
