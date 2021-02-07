print("""
37. Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.
""")

valor_do_produto = float(input('Insira o valor do produto, para receber 12% de desconto: '))
desconto = valor_do_produto - ((valor_do_produto / 100) * 12)
print(f'O valor do produto com o desconto é {desconto} .')
