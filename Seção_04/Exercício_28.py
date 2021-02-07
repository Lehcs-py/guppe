print("""
28. Faça A leitura de três valores e apresente como resultado A soma dos quadrados dos três valores lidos.
""")

num1, num2, num3 = int(input('Insira o 1° valor: ')), int(input('Insira o 2° valor: ')), int(input('Insira o 3° valor: '))
soma_dos_quadrados = ((num1 ** 2) + (num2 ** 2) + (num3 ** 2))
print(f'A soma dos quadrados de {num1}, {num2} e {num3} é {soma_dos_quadrados}.')
