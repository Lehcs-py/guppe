print("""
17. Faça um programa que leia um número inteiro positivo N e calcule A soma dos N primeiros números naturais.
""")

numero = int(input('Insira o número: '))
soma = 0
for num in range(numero):
    soma += num

print(f'A soma dos primeiro numero naturais é: {soma}')
