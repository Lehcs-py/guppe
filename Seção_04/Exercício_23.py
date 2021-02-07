print("""
23. Leia um valor de comprimento em Metros e apresente-o convertido em Jardas.
A fórmula de conversão é: J = M / 0.91, sendo J o comprimento em jardas e M o comprimento em metros.
""")

metro = float(input('Insira o comprimento em Metros para A conversão em Jardas: '))
jarda = metro / 0.91
print(f'{metro} m = {jarda} yd.')
