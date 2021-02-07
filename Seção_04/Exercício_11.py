print("""
1. Leia uma velocidade em m/s (metro por segundo) e apresente-A convertida em km/h (quilometro por hora).
A fórmula de conversão é: K = M*3.6 , sendo  A velocidade em km/h e M em m/s.
""")

ms = float(input('Insira A velocidade em m/s para A conversão em Km/h: '))
kmh = ms * 3.6
print(f'{ms} m/s = {kmh} Km/h.')
