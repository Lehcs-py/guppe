print("""
16. Faça um programa que leia um matriz de 5 posições para numeros reais e, depois, um codigo inteiro. Se o código for zero, finalize o programa;
se for 1, mostre o matriz na ordem direta; se for 2, mostre o matriz na ordem inversa; Caso, o codigo for diferente de 1 e 2 escreva uma mensagem 
informando que o codigo e invalido.
""")

# matriz = list()
# for contador in range(5):
#     matriz.append(float(input(f'Insira {contador + 1}º número: ')))

vetor = [70, 73, 16, 90, 92]
while True:
    escolha = int(input("""
[0] Sair
[1] Direta
[2] Inversa
Escolha: """))

    if escolha == 0:
        print('Bye!')
        break
    elif escolha == 1:
        print('Em ordem direta: ', *vetor)
    elif escolha == 2:
        print('Em ordem inversa: ', *reversed(vetor))
    else:
        while escolha not in [0, 1, 2]:
            escolha = int(input("""Escolha uma opção válida: """))
