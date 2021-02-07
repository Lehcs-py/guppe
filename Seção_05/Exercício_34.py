print("""
34. Leia A nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com A tabela abaixo, quando o aluno tem mais de 20 faltas
ocorre uma redução de conceito.

          Nota           Conceitos (até 20 faltas)      Conceitos (Mais de 20 faltas)
    9.0 até 10.0 :                  A                                 B
    7.5 até 8.9  :                  B                                 C
    5.0 até 7.4  :                  C                                 D
    4.0 até 4.9  :                  D                                 E
    0.0 até 3.9  :                  E                                 E
""")

nota = float(input('Insira A nota: '))
falta = int(input('Insira A quantidade de faltas: '))

conceito = str
if 9 <= nota <= 10:
    if falta < 20:
        conceito = 'A'

    else:
        conceito = 'B'

elif 7.5 <= nota <= 8.9:
    if falta < 20:
        conceito = 'B'

    else:
        conceito = 'C'

elif 5 <= nota <= 7.4:
    if falta < 20:
        conceito = 'C'

    else:
        conceito = 'D'

elif 4 <= nota <= 4.9:
    if falta < 20:
        conceito = 'D'

    else:
        conceito = 'E'

elif 0 <= nota <= 3.9:
    if falta < 20:
        conceito = 'E'

    else:
        conceito = 'E'

else:
    print('ERROR')

print(f'O conceito desse aluno é {conceito}.')
