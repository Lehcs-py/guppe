print("""
13. Faça um programa que receba A temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule A média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
""")

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
medias = list()

for num in range(12):
    media_mes = int(input(f'{meses[num]}: '))
    medias.append(media_mes)

media = (sum(medias) / 12)

print('\nOs meses acima da média foram: ')
for indice, m in enumerate(medias):
    if media < m:
        print(meses[indice], end=' ')
    else:
        pass
