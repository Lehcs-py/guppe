print("""
14. A nota final de um estudante é calculada A partir de três notas atribuidas entre o intervalo de 0 até 10,
respectivamente, A um trabalho de laboratório, A uma avaliação semestral A um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos:
Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5.
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9),
de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessários.
""")

t_d_l = float(input('Insira A nota do trabalho de laboratório: '))
a_s = float(input('Insira A nota da avaliação semestral: '))
e_f = float(input('Insira A nota do exame final: '))

media = ((t_d_l * 2) + (a_s * 3) + (e_f * 5)) / 10

if 0 <= media <= 2.9:
    print(f'Sua média {media} não foi o suficiente, está reprovado.')

elif 3 <= media <= 4.9:
    print(f'Sua média {media} não foi suficiente, está em recuperação.')

elif 10 >= media >= 5:
    print(f'Sua média {media} foi suficiente, está aprovado.')

else:
    print('Um ou mais notas inseridas são inválidas.')
