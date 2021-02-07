print("""
9. Leia uma temperatura em graus Celsius e apresente-A convertida em graus Kelvin.
A fórmula de conversão é: K = C + 273.15, sendo C A temperatura em Celsius e K A temperatura em Kelvin.
""")

celsius = float(input('Insira A temperatura em Celsius para A conversão em Kelvin: '))
kelvin = celsius + 273.15
print(f'{celsius} C° = {kelvin} K.')
