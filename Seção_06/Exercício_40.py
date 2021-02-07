print("""
40. Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo.
O programa tem que retornar o maior e o menor número lido.
""")

num = maior = menor = 0
while True:
    num += 1
    numero = int(input(f'Insira o {num}° número (negativo para parar): '))

    if numero >= 0:
        if num == 1:
            maior = menor = numero

        else:
            if numero > maior:
                maior = numero

            if numero < menor:
                menor = numero

            else:
                pass

    else:
        break

print(f'\nMaior número lido: {maior}\n'
      f'Menor número lido: {menor}')
