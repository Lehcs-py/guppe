print("""
5. Leia um matriz de 10 posições. Contar e escrever quantos valores pares ele possui.
""")

# vetor_ini = input('Insira o matriz: ').split()
vetor_fin = list()
vetor_ini = [4, 44, 72, 7, 3, 21, 99, 6, 9, 21]  # Exemplo.
contador_par = 0

for numero in vetor_ini:
    valor = int(numero)
    vetor_fin.append(valor)
    if valor % 2 == 0:
        contador_par += 1

    else:
        pass

print(f'Em {vetor_fin} foram encontrados {contador_par} valores pares.')
