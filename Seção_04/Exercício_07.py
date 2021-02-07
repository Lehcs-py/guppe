print("""
7. Leia uma temperatura em graus Fahrenheit e apresente-A convertida em graus Celsius.
A fórmula de conversão é: C = 5*(f-32)/9, Sendo C A temperatura em Celsius e F A temperatura em Fahrenheit.
""")

fahrenheit = float(input('Insira A temperatura em Fahrenheit para A conversão em Celsius: '))
celsius = 5 * (fahrenheit - 32) / 9
print(f'{fahrenheit} F° = {celsius} C°.')
