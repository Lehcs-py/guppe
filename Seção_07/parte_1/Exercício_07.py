print("""
7. Escreva um programa que leia 10 números inteiros e os armazene em um matriz. 
Imprima o matriz, o maior elemento e A posição que ele se encontra.
""")

# matriz = input('Insira o matriz: ').split()
vetor = [4, 44, 72, 7, 3, 21, 99, 6, 9, 21]  # Exemplo.
contador_par = 0

print(f'Vetor: {vetor}')
print(f'Maior valor encontrado: {max(vetor)}')
print(f'Posição do maior valor encontrado : {vetor.index(max(vetor))}')
