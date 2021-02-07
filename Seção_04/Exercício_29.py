print("""
29. Leia quatro notas, calcule A média aritmética e imprima o resultado.
""")

nota1 = float(input('Insira A primeira nota: '))
nota2 = float(input('Insira A segunda nota: '))
nota3 = float(input('Insira A terceira nota: '))
nota4 = float(input('Insira A quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A media das notas {nota1}, {nota2}, {nota3} e {nota4} é {media}')
