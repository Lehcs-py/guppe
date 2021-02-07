print("""
 15. Faça um programa que leia um número indeterminado de valores, correspondentes A notas, encerrando A entrada de dados quando for informado um
 valor igual A -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    Mostre A quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre A soma dos valores;
    Calcule e mostre A média dos valores;
    Calcule e mostre A quantidade de valores acima da média calculada;
    Calcule e mostre A quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;
""")

valores = list()
contador = contador_maior = contador_sete = 0
while True:
    valor = int(input(f'Insira o {contador + 1}° valor: '))
    if valor == -1:
        break
    else:
        valores.append(valor)
        contador += 1

print(f'\nForam lidos {contador} valores.')
print(*valores)

inverso_valores = valores
inverso_valores.reverse()
for ind in range(contador):
    print(inverso_valores[ind])

print(f'Soma dos valores: {sum(valores)}.')
print(f'Média dos valores lidos: {(sum(valores) / contador)}.')
for indice, valor in enumerate(valores):
    if valor > (sum(valores) / contador):
        contador_maior += 1
    else:
        pass

for indice, valor in enumerate(valores):
    if valor < 7:
        contador_sete += 1
    else:
        pass

print(f'Foram lidos {contador_maior} valores acima da média.')
print(f'Foram lidos {contador_sete} valores abaixo de sete.')

print('Fim do programa!')
