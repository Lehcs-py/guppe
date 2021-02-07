print("""
26. Leia A distância em Km e A quantidade de litros de gasolina consumidos por um carro em percurso,
calcule o consumo em Km/l e escreva uma mensagem de acordo com A tabela abaixo:
    Consumo   :   Km/l  :    Mensagem
    menor que :    8    :  Venda o carro!
    entre     : 8 e 14  :   Econômico!
    maior que :   12    : Super econômico!
""")

km = float(input('Insira A distância em KM: '))
litros = float(input('Insira A quantidade de litros de gasolina gastos no percurso: '))

consumo = km / litros

print(f'Consumo: Km/l{consumo}')
print()

if consumo < 8:
    print('Venda o carro!')

elif 8 <= consumo <= 14:
    print('Econômico!')

elif consumo > 12:
    print('Super econômico!')

else:
    print('Tem algo de errado!')
