print("""
8. Leia uma temperatura em graus Kelvin e apresente-A convertida em  graus Celsius.
A fórmula de conversão é: C = K - 273.15, sendo C A temperatura em Celsius e K A temperatura em Kelvin.
""")

kelvin = float(input('Insira A temperatura em Kelvin para A conversão em celsius: '))
celsius = kelvin - 273.15
print(f'{kelvin} K = {celsius} C°.')
