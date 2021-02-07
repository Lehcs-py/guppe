print("""
3. Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0. Mostrar uma
 mensagem "FIM!" após A contagem.
""")

for num in range(10, -1, -1):
    if num == 0:
        print('Fim!')
    else:
        print(num)
