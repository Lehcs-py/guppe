print("""
14. Leia um ângulo em Graus e apresente-o convertido em Radianos.
A fórmula de conversão é: R = G*pi/180, sendo G o  ângulo em graus e R em radianos e pi = 3.14 .
""")

grau = float(input('Insira o valor do ângulo em Graus pra A conversão em Radianos: '))
pi = 3.14
radiano = grau * pi / 180
print(f'{grau}° = {radiano} Rad.')
