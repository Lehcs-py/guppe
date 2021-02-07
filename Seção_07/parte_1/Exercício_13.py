print("""
13. Fazer um programa para ler 5 valores e, em seguida, mostrar A posição onde se encontram o maior e o menor valor.
""")

# matriz = list()
# for contador in range(5):
#     matriz.append(float(input(f'Insira {contador + 1}º número: ')))

vetor = [11, 94, 61, 6, 62]  # Exemplo
print(f'Maior: {max(vetor)} Posição: {vetor.index(max(vetor))}')
print(f'Maior: {min(vetor)} Posição: {vetor.index(min(vetor))}')
