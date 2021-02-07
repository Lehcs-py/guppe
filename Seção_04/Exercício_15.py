print("""
15. Leia um ângulo em Radianos e apresente-o convertido em Graus.
A fórmula de conversão é: G = R*180/pi, sendo G o ângulo em graus e R em radianos e pi = 3.14 .
""")

pi = 3.14
radiano = float(input('Insira o valor do ângulo em Radianos para A conversão em Graus: '))
grau = radiano * 180 / pi
print(f'{radiano} Rad = {grau}°.')
