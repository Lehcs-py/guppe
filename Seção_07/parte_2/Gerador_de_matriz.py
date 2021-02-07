def gerador_matriz(i, j, x, y):
    from random import randint
    matriz = list()
    for _ in range(i):
        lista = [randint(x, y) for _ in range(j)]
        matriz.append(lista)
    return matriz


print(gerador_matriz(int(input('i: ')), int(input('j: ')), int(input('X: ')), int(input('Y: '))))
