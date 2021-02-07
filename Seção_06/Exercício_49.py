print("""
49. O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale A um terço do seu salário.
Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está rendendo
2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês. Construa um programa
que deverá calcular e mostrar A quantidade de meses necessários para que o valor pertencente A João iguale ou ultrapasse o valor
pertencente A Carlos. Teste com outros valores para as taxas.
""")

# inv = investimento

carlos = int(input('Insira o salário de Carlos: '))
joao = carlos / 3
contador = inv_carlos = inv_joao = 0

while True:
    inv_carlos += ((carlos / 100) * 2)
    inv_joao += ((joao / 100) * 5)
    contador += 1

    if inv_carlos == inv_joao:
        print(f'{inv_carlos} = {inv_joao}')
        break

    else:
        pass
