print("""
43. Faça um programa que leia um número indeterminado de idades de indivíduos 
(pare quando for informada A idade 0), e calcule A idade média desse grupo.
""")

numero = 1
contador = 1
soma = 0
while True:
    numero = int(input(f'Insira A {contador}° idade (0 para): '))
    if numero > 0:
        soma += numero
        contador += 1
    else:
        break

media = soma / (contador - 1)
print(f'A media da idade desse grupo é: {media}')
