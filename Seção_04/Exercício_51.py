print("""
51. Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0, 0).
""")

x, y = int(input('Insira A coordenada x: ')), int(input('Insira A coordenada y: '))
distancia = (((x ** 2) + (y ** 2)) ** 0.5)
print(f'A distancia entre o ponto x e y é: {distancia}.')
