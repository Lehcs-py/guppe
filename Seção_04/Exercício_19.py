print("""
19. Leia um valor de volume em Litros e apresente-o convertido em Metros Cúbicos m³.
A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros cúbicos.
""")

litro = float(input('Insira o valor do volume em Litros para A conversão em Metros Cúbicos: '))
metro_cubico = litro / 1000
print(f'{litro} l = {metro_cubico} m³.')
