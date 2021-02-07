print("""
15. Leia uma matriz 5 x 10 que se refere respostas de 10 questões de múltipla escolha, referentes A 5 alunos. Leia também um matriz de 10 posições
contendo o gabarito de respostas que podem ser A, B, c ou d. Seu programa deverá comparar as respostas de cada candidato com o gabarito e emitir um
matriz denominado resultado, contendo A pontuação correspondente A cada aluno.
""")

matriz = [[3, 2, 4, 3, 4, 4, 3, 1, 1, 4], [3, 4, 2, 4, 2, 1, 3, 1, 2, 2], [3, 1, 1, 1, 4, 4, 2, 3, 1, 4], [1, 1, 2, 3, 1, 4, 4, 3, 3, 1], [1, 4, 2, 1, 1, 2, 3, 4, 2, 4]]
comp = len(matriz)

for linha in range(comp):  # Transforma as respostas de números para letras.
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] == 1:
            matriz[linha][coluna] = 'A'

        elif matriz[linha][coluna] == 2:
            matriz[linha][coluna] = 'B'
        
        elif matriz[linha][coluna] == 3:
            matriz[linha][coluna] = 'c'
        
        elif matriz[linha][coluna] == 4:
            matriz[linha][coluna] = 'd'
        
        else:
            pass

gabarito = ['c', 'A', 'A', 'A', 'd', 'd', 'B', 'c', 'A', 'd']
pontos = 0
alunos = dict()

for linha_resposta in range(len(matriz)):
    for resposta in range(len(matriz[linha_resposta])):
        if gabarito[resposta] == matriz[linha_resposta][resposta]:
            pontos += 1
        else:
            pass
    alunos[linha_resposta + 1] = pontos
    pontos = 0

for aluno, nota in alunos.items():
    print(f'{aluno}° aluno, Nota: {nota}')

