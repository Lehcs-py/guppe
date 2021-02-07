print("""
3. Ler um conjunto de números reais, armazenando-o em matriz e calcular o quadrado das componentes deste matriz, armazenando o resultado em outro matriz.
Os conjuntos tém 10 elementos cada Imprimir todos os conjuntos.
""")

numeros = list()
quadrados = list()
for num in range(10):
    numero = float(input(f'Insira o {num + 1}º número: '))
    quadrado = (numero ** 2)
    numeros.append(numero)
    quadrados.append(quadrado)

print(f'Vetor: {numeros}')
print(f'quadrados: {quadrados}')
