print("""
51. Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de 1.5%.
A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça programa que determine o salário atual do funcionário.
""")

salario_variavel = 2000
salario_final = 0
porcento = 0.75
for num in range((2021 - 1995) + 1):
    porcento *= 2
    salario_final = (salario_variavel + ((salario_variavel / 100) * porcento))
    salario_variavel = salario_final

print(f'Salário final: {salario_final}')
