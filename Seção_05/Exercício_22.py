print("""
22. Leia A idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
As condições para aposentadoria são
    Ter pelo menos 65 anos,
    Ou ter trabalhado pelo menos 30 anos,
    Ou ter pelo menos 60 aos e trabalhado pelo menos 25 anos.
""")

idade = int(input('Insira A idade: '))
tempo_servico = int(input('Insira o tempo serviço: '))
print('')

c = 0
if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 30):
    print('Aposentadoria concedida.')

else:
    print('Aposentadoria negada.')
