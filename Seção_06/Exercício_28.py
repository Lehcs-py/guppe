print("""
28. Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E, conforme A fórmula A seguir
    E = 1+ 1/1!+ 1/2! + 1/3! + ... + 1/N!
""")

numero = int(input('Insira o número: '))

soma_e = 0
fatorial = 1
for num in range(1, numero + 1):
    for n in range(1, num + 1):
        fatorial *= n
    soma_e += 1 / fatorial

print(f'H({numero}) = {soma_e}')
