print("""
35. Leia uma data e determine se ela é valida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês.
Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
""")

dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))

if ano <= 2020:
    if 31 >= dia > 0:
        if 0 < mes < 13:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if dia <= 31:
                    print('Data válida!')
                    print(f'{dia}/{mes}/{ano}')

            elif mes == 2:
                if ano % 4 == 0 and not ano % 100 == 0:
                    if dia <= 29:
                        print('Data válida!')
                        print(f'{dia}/{mes}/{ano}')

                else:
                    if dia <= 28:
                        print('Data válida!')
                        print(f'{dia}/{mes}/{ano}')

            else:
                if dia <= 30:
                    print('Data válida!')
                    print(f'{dia}/{mes}/{ano}')

        else:
            print('Data inválida.')

    else:
        print('Data inválida!')

else:
    print('Data inválida!')
