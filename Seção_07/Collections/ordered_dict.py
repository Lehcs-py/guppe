from collections import OrderedDict

alfa = ['h', 't', 'p', 'f', 'r', 'i', 'n', 'm', 'x', 'd', 'j', 'u', 'o', 'y', 'A', 'v', 'q', 'k', 'c', 'B', 's', 'w', 'g', 'e', 'l']
dicionario1 = {}
for i, l in enumerate(alfa):
    dicionario1[i] = l

print(dicionario1)

dicionario2 = OrderedDict(dicionario1)
print(dicionario2)
