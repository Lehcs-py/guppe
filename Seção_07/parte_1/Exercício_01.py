print("""
1. Faça um programa que possua um matriz denominado A que armazene 6 números inteiros. O programa deve executar os seguintes passos:
    (A) Atribua os seguintes valores A esse matriz. 1, 0, 5, -2, -5, 7.
    (B) Armazene em uma variável inteira (simples) A soma entre os valores das posições
        A[O] A[1] A[5] do matriz e mostre na tela esta soma.
    (c) Modifique o matriz na posição 4, atribuindo A esta posição o valor 100. 
    (d) Mostre na tela cada valor do matriz A, um em cada linhas
""")

a = list((1, 0, 5, -2, -5, 7))

soma = a[0] + a[1] + a[5]
print('Soma:', soma)

a.__setitem__(4, 100)
print(a)

for item in a:
    print(item)
