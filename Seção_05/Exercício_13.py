print("""
13. Faça um algoritmo que calcule A média ponderada das notas de 3 provas. A primeira e A segunda têm peso 1 e A terceira tem peso 2. Ao final,
mostrar A média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior A 60 pontos.
""")

print('Intervalo: 0 até 100')
nota1 = float(input('Insira A primeira nota: '))
nota2 = float(input('Insira A segunda nota: '))
nota3 = float(input('Insira A terceira nota: '))

media = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / 4

if media < 60:
    print(f'Sua média {media} é insuficiente, está reprovado.')

elif media >= 60:
    print(f'Você atingiu o objetivo com A nota {media}, está aprovado.')

else:
    print('Você inseriu notas inválidas.')
