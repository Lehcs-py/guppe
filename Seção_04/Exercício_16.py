print("""
16. Leia um valor de comprimento em Polegadas e apresente-o convertido em Centímetros.
A formula de conversão é: C = P*2.54, sendo C o comprimento em centímetro e P o comprimento em polegadas.
""")

polegada = float(input('Insira o comprimento em Polegadas para A conversão em Centímetros: '))
centimetro = polegada * 2.54
print(f'{polegada} in = {centimetro} cm.')
