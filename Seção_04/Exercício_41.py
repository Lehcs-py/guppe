print("""
41. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor A ser pago ao
 funcionário, adicionado 10% sobre o valor do calculado.
""")

valor_da_hora = float(input('Insira o valor da hora trabalhada: '))
hora_trabalhada = int(input('Insira A quantidade de horas trabalhadas: '))
pagamento_total = (valor_da_hora * hora_trabalhada) + (((valor_da_hora * hora_trabalhada) / 100) * 10)
print(f'O pagamento total do funcionário é {pagamento_total}.')
