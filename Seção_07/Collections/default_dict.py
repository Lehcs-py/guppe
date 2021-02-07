dicionario1 = {'amiga': 'Annubis'}

print(dicionario1)
print(dicionario1["amiga"])
# print(dicionario1['outro'])

from collections import defaultdict

dicionario2 = defaultdict(lambda: 0)
dicionario2["amiga"] = 'Annubis'

print(dicionario2["amiga"])
print(dicionario2["amigo"])

print('https://docs.python.org/pt-br/3/library/collections.html?highlight=collections')
print('https://docs.python.org/pt-br/3/library/collections.html?highlight=collections#collections.defaultdict')
