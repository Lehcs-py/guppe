print("""
32. Escrever um programa que leia o código do produto escolhido de uma lanchonete e A quantidade.
O programa deve calcular o valor A ser pago por aquele lanche. Considere que A cada exceção somente
será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:

    Especificação  : Código:    Preço
    Cachorro Quente:  100  :   R$ 1.20
    Bauru Simples  :  101  :   R$ 1.30
    Bauru com Ovo  :  102  :   R$ 1.50
    Hamburguer     :  103  :   R$ 1.20
    Cheeseburguer  :  104  :   R$ 1.70
    Suco           :  105  :   R$ 2.20
    Refrigerante   :  106  :   R$ 1.00
""")

cod = int(input('''

    Especificação  : Código:    Preço
    Cachorro Quente:  100  :   R$ 1.20
    Bauru Simples  :  101  :   R$ 1.30
    Bauru com Ovo  :  102  :   R$ 1.50
    Hamburguer     :  103  :   R$ 1.20
    Cheeseburguer  :  104  :   R$ 1.70
    Suco           :  105  :   R$ 2.20
    Refrigerante   :  106  :   R$ 1.00

Insira o código do produto: 
'''))
quantidade = int(input('Insira A quantidade: '))
total = int

if cod == 100:
    custo = 1.20*quantidade
    total += custo

elif cod == 101:
    custo = 1.30*quantidade
    total += custo

elif cod == 102:
    custo = 1.50*quantidade
    total += custo

elif cod == 103:
    custo = 1.20*quantidade
    total += custo

elif cod == 104:
    custo = 1.70*quantidade
    total += custo

elif cod == 105:
    custo = 1.50*quantidade
    total += custo

elif cod == 106:
    custo = 1.00*quantidade
    total += custo

else:
    print('Tem algo de errado...')

print(f'O total é R${total}')
