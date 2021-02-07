print("""
38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano. Teste A
validade desta data para saber se está é uma data válida. Teste se o dia fornecido é um dia válido: dia >0, dia 28 para
o mês de fevereiro (29 e o ano for bissexto), dia <= 30 em abril, junho, setembro e novembro, dia <= 31 nos outros
meses. Teste A validade do mês > 0 e mês < 13. Teste A validade do ano <= ano atual (use uma constante definida
com o valor igual A 2008). Imprimir: "data válida" ou "data inválida" no final da execução do programa.
""")

nascimento = int(input('dd/mm/aaaa'))
