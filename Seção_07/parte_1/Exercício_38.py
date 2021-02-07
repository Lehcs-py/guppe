print("""
38. Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, guardando-os num matriz.
Ordene o valor assim que ele for digitado. Mostre ao final na tela os valores em ordem.
""")

vetor = list()
for contador in range(10):
    vez = 0
    numero = int(input(f'Insira {contador + 1}º número: '))
    if contador == 0:
        vetor.append(numero)
    elif contador == 1:
        if vetor[0] < numero:
            vetor.append(numero)
        elif vetor[0] > numero:
            vetor.insert(0, numero)
    else:
        for ind, num in enumerate(vetor):
            print(num)
            if num > numero:
                vez += 1
                print(vez)
            vetor.insert(vez, )


print(vetor)
