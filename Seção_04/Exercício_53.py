print("""
53. Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.
""")

l, c = float(input('Insira A largura do terreno: ')), float(input('Insira o comprimento do terreno: '))
perimetro = (l * 2) + (c * 2)
custo_da_tela = float(input('Insira o valor do metro de tela: R$'))
custo = perimetro * custo_da_tela
print(f'O custo total par cercar esse terreno com tela é {custo} .')
