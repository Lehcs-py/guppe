print("""
40. Uma empresa contrata um encanador A R$ 30 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima
 A quantia liquida que deverá ser paga, sabendo-se que serão descontados 8% para imposto de renda.
""")

dias_trabalhados = int(input('Insira A quantidade de dias trabalhados: '))
pagamento = (dias_trabalhados * 30) - (((dias_trabalhados * 30) / 100) * 8)
print(f'O pagamento do encanador é: {pagamento}')
