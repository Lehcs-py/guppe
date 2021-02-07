print("""
3. Faça um Programa que leia 4 notas, mostre as notas e A média na tela.
""")

notas = list()
for num in range(4):
    nota = float(input(f'Insira A {num + 1}° nota: '))
    notas.append(nota)

print(f'Média: {sum(notas) / 4}')
