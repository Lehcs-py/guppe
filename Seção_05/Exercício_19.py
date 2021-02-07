print("""
19. Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.
""")

num = int(input('Insira um número para verificar se ele é divisível por 3 ou 5, mas não pelos dois: '))

if num % 3 == 0 and not num % 5 == 0:
    print('Número divisível por 3.')

elif num % 5 == 0 and not num % 3 == 0:
    print('Número divisível por 5.')

elif num % 3 == 0 and num % 5 == 0:
    print('Número divisível pelos dois.')

else:
    print('Número não divisível por nenhum dos dois.')
