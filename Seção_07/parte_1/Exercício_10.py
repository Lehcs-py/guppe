print("""
10. Faça um programa para ler A nota da prova de 15 alunos e armazene num matriz, calcule e imprima A media geral. 
""")
notas = [8, 5, 6, 8, 6, 10, 7, 7, 10, 8, 10, 10, 5, 6, 8]  # Exemplo
# notas = list()
# for contador in range(15):
#    notas.append(float(input(f'Insira A nota do {contador + 1}º aluno: ')))

print(f'A média geral desses 15 alunos é: {sum(notas)}/{len(notas)} = {sum(notas) / len(notas)}')
