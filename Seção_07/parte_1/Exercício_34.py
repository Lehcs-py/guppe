print("""
34. Faça um programa para ler 10 números DIFERENTES A serem armazenados em um matriz. Os dados deverão ser armazenados no matriz na ordem que forem
sendo lidos, sendo que caso o usuário digite um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número.
Note que cada valor digitado pelo usuário deve ser pesquisado no matriz, verificando se ele existe entre os números que já foram fornecidos. Exibir
na tela o matriz final que foi digitado.
""")

vetor = list()
for contador in range(10):
    numero = int(input(f'Insira {contador + 1}º número: '))
    if vetor.__contains__(numero):
        while vetor.__contains__(numero):
            numero = int(input(f'Insira um número diferente dos anteriores: '))
        vetor.append(numero)

    else:
        vetor.append(numero)

print(vetor)
