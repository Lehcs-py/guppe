print("""
19. Faça um matriz de tamanho 50 preenchido com o seguinte valor: (i + 5 * i)%(i + 1), sendo i A posição do elemento no matriz.
Em seguida imprima o matriz na tela.
""")

vetor = list()

for i in range(50):
    print((i + 5 * i) % (i + 1), end=' ')
