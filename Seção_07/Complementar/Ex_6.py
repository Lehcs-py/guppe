print("""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num matriz A média de cada aluno,
imprima o número de alunos com média maior ou igual A 7.0.
""")

medias = list()
for num1 in range(10):
    notas = list()
    print(f'Para o {num1 + 1} aluno: ')
    for num2 in range(4):
        nota = float(input(f'{num2 + 1}° nota: '))
        notas.append(nota)

    media = (sum(notas) / 4)
    medias. append(media)
    print()

contador = 0
for aluno, media in enumerate(medias):
    if media >= 7:
        contador += 1

    else:
        pass

print(f'{contador} alunos ficaram com média igual ou maior A 7.')
