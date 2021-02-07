print("""
37. As tarifas de certo parque de estacionamento são as seguintes:

    1ª e 2ª hora - R$ 1.00 cada
    3ª e 4ª hora - R$ 1.40 cada
    5ª hora e seguintes  - R$ 2.00 cada

    O número de horas A pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas,
    que é o mesmo que pagaria se tivesse estacionado por 120 minutos. Os momentos de chegada ao parque e A partida deste são apresentados na
    forma de pares inteiros, representando horas e minutos. Por exemplo, o par 12 50 representará "dez para uma da tarde". Pretende-se criar um
    programa que, lidos pelo teclado os momentos de chegada e de partida, escreva tela o preço cobrado pelo estacionamento. Admite-se que A
    chegada  e A partida se dão com intervalo não superior A 24 horas. Portanto, se uma dada hora de chegada for superior á da partida, isso não é
     uma situação de    erro, antes significará que A partida ocorreu dia seguinte ao da chegada.
""")

chegada = input('Insira A hora de chegada (hh mm): ').strip()
saida = input('Insira A hora de saída (hh mm): ').strip()
calculo = (float(saida[0:2]) - float(chegada[0:2])) + ((float(saida[3:5]) - float(chegada[3:5]))/100)
horas = calculo

if chegada < saida:
    if 0 < horas >= 2:
        valor = 0
        if 0 < horas >= 1:
            valor += 1

        else:
            valor += 2

    if 2 < horas >= 4:
        valor = 2

        if 2 < horas >= 3:
            valor += 1.40

        else:
            valor += 2.80

    if 4 < horas:
        valor = 4.80
        valor += (horas - 4)*2

    print(f'Valor A ser pago: R${valor}')
else:
    print('Você extrapolou o limite... o valor A ser pago é de R$200.00')