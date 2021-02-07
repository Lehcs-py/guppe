print("""
26. Leia um valor de área em Metros Quadrados m² e apresente-o convertido em Hectares.
A fórmula de conversão é: H = M * 0.0001, sendo M A área em metros quadrados e H A área em hectares.
""")

metro_quadrado = float(input('Insira o valor da área em Metros Quadrados para A conversão em Hectares: '))
hectare = metro_quadrado * 0.0001
print(f'{metro_quadrado} m² = {hectare} ha.')
