print("""
36. Escreva um programa que, dado o valor da venda, imprima A comissão que deverá ser paga ao vendedor. Para calcular A comissão, considere A tabela abaixo:

                        Venda mensal                                                                                               Comissão
    Maior ou igual A R$ 100_000.00                                                              : R$ 700.00 + 16% das vendas
    Menor que R$ 100_000.00 e maior ou igual A R$ 80_000.00      : R$ 650.00 + 14% das vendas
    Menor que R$ 80_000.00 e maior ou igual A R$ 60_000.00        : R$ 600.00 + 14% das vendas
    Menor que R$ 60_000.00 e maior ou igual A R$ 40_000.00        : R$ 550.00 + 14% das vendas
    Menor que R$ 40_000.00 e maior ou igual A R$ 20_000.00        : R$ 500.00 + 14% das vendas
    Menor que R$ 20_000.00                                                                           : R$ 400.00 + 14% das vendas
""")

valor_venda = int(input('Insira o valor da venda: '))

comissao = str
if valor_venda >= 100_000:
    comissao = 700 + ((valor_venda/100)*16)

elif 100_000 > valor_venda >= 80_000:
    comissao = 650 + ((valor_venda/100)*16)

elif 80_000 > valor_venda >= 60_000:
    comissao = 600 + ((valor_venda / 100) * 14)

elif 60_000 > valor_venda >= 40_000:
    comissao = 550 + ((valor_venda / 100) * 14)

elif 40_000 > valor_venda >= 20_000:
    comissao = 500 + ((valor_venda / 100) * 14)

elif 20_000 > valor_venda:
    comissao = 400 + ((valor_venda / 100) * 14)

else:
    comissao = 0

print(f"A comissão desse vendedor é de R${comissao}")
