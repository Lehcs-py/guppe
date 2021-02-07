print("""
42. Receba o salário-base de um funcionário. Calcule e imprima o salário A receber, sabendo-se que esse funcionário tem uma gratificação de 5%
 sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário base.
""")

salario_base = float(input('Insira o salário-base do funcionário: '))
desconto = salario_base - ((salario_base/100) * 7)
salario = desconto + ((salario_base/100) * 5)
print(f'O salario desse funcionário é {salario}')
