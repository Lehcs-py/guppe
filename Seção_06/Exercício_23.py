print("""
23. Faca um algoritmo que leia um número positivo e imprima seus divisores.
""")

numero = int(input('Insira o número: '))
print('\nSeus divisores são:')
for num in range(1, numero + 1):
    if numero % num == 0:
        print(num)

    else:
        pass
