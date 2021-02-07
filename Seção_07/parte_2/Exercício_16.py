print("""
16. Faça um programa para corrigir uma prova com 10 questões de múltipla escolha (A, B, c, d ou e), em uma turma com 3 alunos.
Cada questão vale 1 ponto. Leia o gabarito, e para cada aluno leia sua matricula (número inteiro) e suas respostas.
Calcule e escreva: Para cada aluno, escreva sua matrícula, suas respostas, e sua nota. O percentual de aprovação, assumindo média 7.0.
""")

gabarito = ['c', 'A', 'A', 'A', 'd', 'd', 'B', 'c', 'A', 'd']
pontos = 0
alunos = dict()
notas = dict()

turma = range(int(input('Quantos alunos na turma: ')))
print()

for aluno in turma:
    print(f'{aluno + 1}° aluno'.center(20, '_'))
    matricula = int(input('Número da matricula: '))
    alunos[matricula] = list()
    for questao in range(10):
        alunos[matricula].append(input(f'{questao +  1}º questão: '))

for matri, resps in alunos.items():  # matri = matricula, resps = respostas
    for ind, resp in enumerate(resps):  # resp = resposta
        if resp == gabarito[ind]:
            pontos += 1
        else:
            pass
    notas[matri] = pontos
    pontos = 0


print('\n', gabarito)
for matri, resps in alunos.items():
    print(f'Matricula {matri};', 'Respostas', *resps, ';', f'Nota {notas[matri]}')
