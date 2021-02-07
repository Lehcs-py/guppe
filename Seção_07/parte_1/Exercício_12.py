print("""
12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e A média dos valores.
""")

# matriz = list()
# for contador in range(5):
#     matriz.append(float(input(f'Insira {contador + 1}º número: ')))

vetor = [115, 88, 93, 113, 118]  # Exemplo

print(f'Vetor: {vetor}')
print(f'Max: {max(vetor)}')
print(f'Min: {min(vetor)}')
print(f'Média: {sum(vetor)/len(vetor)}')
