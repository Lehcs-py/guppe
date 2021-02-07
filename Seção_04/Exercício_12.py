print("""
12. Leia uma distancia em milhas e apresente-A convertida em quilômetros.
A fórmula de conversão é: K = 1.61*M, sendo K A distancia em quilômetro e M em milha.
""")

milha = float(input('Insira A distancia em Milha para A conversão em Quilômetro: '))
km = milha * 1.61
print(f'{milha} mi = {km} km.')
