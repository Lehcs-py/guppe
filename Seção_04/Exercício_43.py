print("""
43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
      O total A pagar com desconto de 10%;
      O valor de cada parcela, no parcelamento de 3x sem juros;
      A comissão do vendedor, no caso da venda A ser A vista (5% sobre o valor com desconto);
      A comissão do vendedor, no caso da venda ser parcelada (5% Sobre o valor total).
""")

valor_do_produto = float(input('Insira o valor do produto: '))
desconto = valor_do_produto - ((valor_do_produto / 100) * 10)
parcelas = valor_do_produto / 3
comissao_a_vista = ((desconto / 100) * 5)
comissao_parcelado = ((valor_do_produto / 100) * 5)

print(f'Desconto: R$ {desconto}\n'
      f'valor parcelado em 3x de: R$ {parcelas}\n'
      f'Comissão A vista: {comissao_a_vista}\n'
      f'Comissão parcelado: {comissao_parcelado}.')
