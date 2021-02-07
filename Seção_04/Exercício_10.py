print("""
10. Leia uma velocidade em Km/h (quilometro por hora) e apresente-A convertida em m/s (metro por segundo).
A fórmula de conversão é: M = K/3.6 , sendo K A velocidade em km/h e M em m/s.
""")

kms = float(input('Insira A velocidade em Km/h para A conversão em m/s: '))
ms = kms / 3.6
print(f'{kms} km/h = {ms} m/s.')
