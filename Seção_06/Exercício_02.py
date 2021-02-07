print("""
2. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar A estrutura de repetição for, A segunda while,
e A terceira do while.
""")

# Usando for.
for num in range(1, 101):
    print(num, end=' ')

print()
print()

# Usando while.
contador = num = 0
while contador != 101:
    num += 1
    print(num, end=' ')
    contador += 1
