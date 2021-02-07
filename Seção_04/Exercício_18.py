print("""
18. Leia um valor de volume em Metros Cúbicos m³ e apresente-o convertido em Litros.
A fórmula de conversão é: L = 1000*M, sendo L o volume em litros e M o volume em metros cúbicos.
""")

metro_cubico = float(input('Insira o valor do volume em Metros Cúbicos para A conversão em Litros: '))
litro = 1000 * metro_cubico
print(f'{metro_cubico} m³ = {litro} l')
