print("""
35. Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste
intervalo e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior
que o valor final) deve ser escrito uma mensagem de erro na tela, "Intervalo de valores inválido" e o programa termina. Exemplo de tela de saída:
    Digite o valor inicial e valor final: 5 10
    Soma dos ímpares neste intervalo: 21
""")

inicio = int(input('Insira o valor inicial: '))
fim = int(input('insira o valor final: '))

soma = 0
if inicio > fim:
    print('Intervalo inválido.')

else:
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            pass

        else:
            soma += num

print(f'Soma dos impares nesse intervalo: {soma}')
