print("""
38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
""")

salario = float(input('Insira o valor do salário: '))
novo_salario = ((salario / 100) * 25) + salario
print(f'O novo salario do funcionário é: {novo_salario}.')
