print("""
16. Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente A este número. Isto é, janeiro se 1,
fevereiro se 2, e assim por diante.
""")

mes = int(input('Insira o número do mês: '))

if mes == 1:
    print('Janeiro')

elif mes == 2:
    print('Fevereiro')

elif mes == 3:
    print('Março')

elif mes == 4:
    print('Abril')

elif mes == 5:
    print('Maio')

elif mes == 6:
    print('Junho')

elif mes == 7:
    print('Julho')

elif mes == 8:
    print('Agosto')

elif mes == 9:
    print('Setembro')

elif mes == 10:
    print('Outubro')

elif mes == 11:
    print('Novembro')

elif mes == 12:
    print('Dezembro')

else:
    print('Mês inválido.')
