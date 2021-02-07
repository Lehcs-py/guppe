print("""
8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e exiba na tela A média dessas notas. Uma nota válida
deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso A nota não possua um valor válido, este fato deve ser informado ao usuário
e o programa termina.
""")

nota1 = float(input('Insira A 1° nota: '))
nota2 = float(input('Insira A 2° nota: '))

if nota1 >= 0 <= nota2 <= 10 >= nota1:
    media = (nota1 + nota2) / 2
    print(f'A média das notas {nota1} e {nota2} é {media}')
else:
    print('Você informou uma ou mais notas invalidas!')
