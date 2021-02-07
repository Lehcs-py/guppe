print("""
22. Leia um valor de comprimento em Jardas e apresente-o convertido em Metros.
A fórmula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
""")

jarda = float(input('Insira o comprimento em Jardas pra A conversão em Metros: '))
metro = 0.91 * jarda
print(f'{jarda} yd = {metro} m.')
