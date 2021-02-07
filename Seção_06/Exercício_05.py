print("""
5. Faça um programa que peça ao usuário para digitar 10 valores e some-os.
""")

soma = 0
for num in range(10):
    numero = int(input(f'Digite o {num+1}° número: '))
    soma += numero

print(f'A soma dos 10 número é {soma}.')
