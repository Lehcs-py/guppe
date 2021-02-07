print("""
46. Faça um programa que leia um número inteiro positivo de três dígitos (de 100 A 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo 123 -> 321.
""")

num = input('Insira um número de 3 algarismos (100 A 999): ')
num_invertido = num[::-1]
print(f'{num} invertido: {num_invertido}.')