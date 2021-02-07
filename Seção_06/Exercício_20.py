print("""
20. Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados lidos e número de valores pares.
O processo termina quando for digitado o número 1000.
""")

contador = contador_par = numero = 0
while numero != 1000:
    numero = int(input('Insira número (1000 para parar): '))
    if numero % 2 == 0:
        contador_par += 1
    else:
        pass
    contador += 1

print(f'Foram digitados {contador} valores, {contador_par} são pares.')
