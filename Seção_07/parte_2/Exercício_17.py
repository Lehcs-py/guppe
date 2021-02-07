print("""
17. Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva o número de alunos cuja pior nota foi na prova 1, o número de
alunos cuja pior nota foi na prova 2, e o número de alunos cuja pior nota foi na prova 3. Em caso de empate das piores notas de um aluno, o critério
de desempate é arbitrário, mas o aluno deve ser contabilizado apenas uma vez.
""")

matriz = [[9, 9, 8], [5, 7, 10], [8, 7, 9], [5, 9, 6], [9, 9, 7], [10, 6, 10], [7, 5, 10], [8, 9, 10], [7, 10, 6], [7, 5, 5]]
p1 = p2 = p3 = 0
alunos = dict()

for i in range(len(matriz)):
    if matriz[i].index(min(matriz[i])) == 0:
        p1 += 1

    elif matriz[i].index(min(matriz[i])) == 1:
        p2 += 1

    elif matriz[i].index(min(matriz[i])) == 2:
        p3 += 1

    else:
        pass

print(f"""
1º prova: {p1}
2º prova: {p2}
3º prova: {p3}
""")
