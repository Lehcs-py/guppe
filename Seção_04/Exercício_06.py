print("""
 6. Leia uma temperatura em graus Celsius e apresente-A convertida em graus Fahrenheit.
 A fórmula de conversão é: F = C*(9/5)+32, sendo F A temperatura em Fahrenheit e C A temperatura em Celsius.
""")

celsius = float(input('Insira A temperatura em Celsius para A conversão em Fahrenheit: '))
fahrenheit = celsius * (9 / 5) + 32
print(f'{celsius} C° = {fahrenheit} F°.')
