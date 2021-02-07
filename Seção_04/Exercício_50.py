print("""
50. Implemente um programa que calcule o ano de nascimento de uma pessoa A partir de sua idade e do ano atual.
""")

idade = int(input('Insira sua idade: '))
ano_atual = int(input('Insira o ano atual: '))
ano_de_nascimento = ano_atual - idade
print(f'O ano do seu nascimento é {ano_de_nascimento}.')
