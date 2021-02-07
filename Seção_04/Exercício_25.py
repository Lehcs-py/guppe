print("""
25. Leia um valor de área em Acres e apresente-o convertido em Metros Quadrados m².
A fórmula de conversão é: M = A*4048.58, sendo M A área em metros quadrados e A A área em acres.
""")

acre = float(input('Insira o valor da área em Acres para A conversão em Metros Quadrados: '))
metro_quadrado = acre * 4048.58
print(f'{acre} ac = {metro_quadrado} m².')