print("""
17. Leia um valor de comprimento em  Centímetros e apresente-o convertido em Polegadas.
A formula de conversão é: P = C/2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
""")

centimetro = float(input('Insira o comprimento em Centímetros para A conversão em Polegadas: '))
polegada = centimetro / 2.54
print(f'{centimetro} cm = {polegada} in.')
