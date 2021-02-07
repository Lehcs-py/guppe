print("""
24. Escreva um programa que leia um número inteiro e calcule A soma de todos os divisores desse número, com exceção dele próprio.
Ex: A soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
""")

soma = 0
numero = int(input('Insira o número: '))
print('\nA soma dos seus divisores são:')
for num in range(1, numero):
    if numero % num == 0:
        print(num, end='')
        print(' + ', end='')
        soma += num
    else:
        pass

print(f' = {soma}')
