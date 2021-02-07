print("""
24. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o produto
(MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne
o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de
erro.
""")

custo = float(input('Insira o custo R$'))
estado = str(input('Escolha o estado (MG; SP; RJ; MS): ')).strip().upper()

if estado == 'MG':
    custo_final = custo + ((custo/100)*7)

elif estado == 'SP':
    custo_final = custo + ((custo / 100) * 12)

elif estado == 'RJ':
    custo_final = custo + ((custo / 100) * 15)

elif estado == 'MS':
    custo_final = custo + ((custo / 100) * 8)

else:
    custo_final = 0

print()

if custo_final > 0:
    print(f'O custo final nesse estado é de R${custo_final}')

else:
    print('Esse não é um estado válido.')
