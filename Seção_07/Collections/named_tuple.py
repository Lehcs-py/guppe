from collections import namedtuple

amiga1 = namedtuple('amiga', 'idade altura nome')
amiga2 = namedtuple('amiga', 'idade, altura, nome')
amiga3 = namedtuple('amiga', ['idade', 'altura', 'nome'])

amiga_1 = amiga1(idade=16, altura=150, nome='Annubis')
print(amiga_1)

amiga_2 = amiga2(idade=16, altura=150, nome='Annubis')
print(amiga_2)

amiga_3 = amiga3(idade=16, altura=150, nome='Annubis')
print(amiga_3)

print('Idade:', amiga_2.idade)
print('Altura:', amiga_2.altura)
print('Nome:', amiga_2.nome)

print('https://docs.python.org/pt-br/3/library/collections.html?highlight=collections')
print('https://docs.python.org/pt-br/3/library/collections.html?highlight=collections#collections.namedtuple')
