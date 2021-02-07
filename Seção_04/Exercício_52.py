print("""
52. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para A realização
 da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com
 base no valor investido.
""")

jogador_1 = float(input('Insira o valor investido pelo 1° jogador: '))
jogador_2 = float(input('Insira o valor investido pelo 2° jogador: '))
jogador_3 = float(input('Insira o valor investido pelo 3° jogador: '))
premio = float(input('Insira o valor do premio: '))

total = jogador_1 + jogador_2 + jogador_3

porcentagem_jogador_1 = (jogador_1/total) * 100
porcentagem_jogador_2 = (jogador_2/total) * 100
porcentagem_jogador_3 = (jogador_3/total) * 100

premio_1 = (premio/100) * porcentagem_jogador_1
premio_2 = (premio/100) * porcentagem_jogador_2
premio_3 = (premio/100) * porcentagem_jogador_3

print(f'''
1° Jogador investiu {porcentagem_jogador_1:.0f}%, e vai receber R$ {premio_1:.2f} .
2° Jogador investiu {porcentagem_jogador_2:.0f}%, e vai receber R$ {premio_2:.2f} .
3° Jogador investiu {porcentagem_jogador_3:.0f}%, e vai receber R$ {premio_3:.2f} .''')
