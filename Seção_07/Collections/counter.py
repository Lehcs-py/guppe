from collections import Counter

lista1 = [63, 78, 88, 92, 99, 100, 7, 3, 21, 7, 3, 21, 7, 3, 21, 7, 3, 21, 7, 3, 21, 7, 3, 21, 7, 3, 21, 7, 3, 21, 7, 3, 21]
counter1 = Counter(lista1)
print(counter1)

str1 = "LUCAS EDUARDO HIGINO CORIOLANO DOS SANTOS"
counter2 = Counter(str1)
print(counter2)

texto = """One Piece (ワンピース Wan Pīsu?) é uma série de mangá escrita e ilustrada por Eiichiro Oda. Os capítulos têm sido serializados na revista 
Weekly Shōnen Jump desde 22 de julho de 1997, com os capítulos compilados e publicados em 96 volumes tankōbon pela editora Shueisha até abril de 
2020. One Piece conta as aventuras de Monkey D. Luffy, um jovem cujo corpo ganhou as propriedades de borracha após ter comido uma fruta do diabo 
acidentalmente. Com sua tripulação, os Piratas do Chapéu de Palha, Luffy explora A Grand Line em busca do tesouro mais procurado do mundo, 
o "One Piece", A fim de se tornar o próximo Rei dos Piratas. """.upper().split()
counter3 = Counter(texto)
# print(counter3)
print(counter3.most_common(7))

print('https://docs.python.org/pt-br/3/library/collections.html?highlight=collections')
print('https://docs.python.org/pt-br/3/library/collections.html?highlight=collections#collections.Counter')
