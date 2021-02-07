print("""
33. Um produto vai sofrer aumento de acordo com A tabela abaixo.
Leia o preço antigo, calcule e escreva o preço novo, e escreva uma
mensagem em função do preço novo (de acordo com A segunda tabela).

    Preço Antigo                 Percentual de Aumento
    até R$ 50                   :                      5%
    entre R$ 50 e 100  :                     10%
    acima de R$ 100   :                     15%

    Preço Novo                                          Mensagem
    até R$ 80                                           :   Barato
    entre R$ 80 e 120 (inclusive)     :     Normal
    entre R$ 120 e 200 (inclusive)  :   Caro
    acima de R$ 200                           :   Muito Caro
""")

p_antigo = float(input('Insira o preço antigo: '))

p_novo = str
if p_antigo <= 50:
    p_novo = (p_antigo + (p_antigo/100)*5)

elif 50 < p_antigo <= 100:
    p_novo = (p_antigo + (p_antigo/100)*10)

elif p_antigo > 100:
    p_novo = (p_antigo + (p_antigo/100)*15)

print(f'O preço novo é {p_novo}')
