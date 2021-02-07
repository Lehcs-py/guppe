print("""
12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à 
média de altura desses alunos.
""")

x = 30
alunos = list()
soma_altura = media = 0
for num in range(x):
    print(f'{num + 1}°'.center(12, '_'))
    idade_altura = (int(input('Idade: ')), int(input('Altura: ')))
    alunos.append(idade_altura)

for indice, aluno in enumerate(alunos):
    soma_altura += aluno[1]

media = (soma_altura / x)

contador = 0
for indice, aluno in enumerate(alunos):
    if aluno[0] > 13 and aluno[1] < media:
        contador += 1

print(f'\n{contador} alunos tem idade superior a 13 anos e possuem altura menor que a média.')
