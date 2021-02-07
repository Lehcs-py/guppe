print("""
40. O custo ao consumidor de um carro novo é A soma do custo de fábrica, da comissão do distribuidor, e dos impostos são
calculados sobre o custo de fábrica, de acordo com A tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.

     Custo de fábrica               | %Do distribuidor |  %Dos impostos
     até R$ 12_000.00               |        5%        |     isento
     entre R$ 12_000.00 e 25_000.00 |        10%       |      15%
     Acima de R$ 25_000.00          |        15%       |      20%
""")
custo_fabrica = float(input('Insira o custo de fábrica: '))

x = y = int
if 0 < custo_fabrica <= 12_000:
    x = 0
    y = 5

elif 12_000 < custo_fabrica <= 25_000:
    x = 15
    y = 10

elif custo_fabrica > 25_000:
    x = 20
    y = 15

imposto = (custo_fabrica/100)*x
custo_final = custo_fabrica + (((custo_fabrica + imposto)/100)*y) + imposto

print(f'O custo final do carro é: R${custo_final}.')
