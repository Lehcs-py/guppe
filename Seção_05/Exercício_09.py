print("""
9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se A prestação for maior que 20% do salário imprima:
Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
""")

salario = float(input('Insira o salário: '))
prestacao = float(input('Insira o valor da prestação: '))

if ((salario/100) * 20) > prestacao:
    print('Empréstimo concedido!')
else:
    print('Empréstimo não concedido!')
