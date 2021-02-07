print("""
22. Escreva um programa completo que permita A qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas (válidas no intervalo de 10 A 20) e que
mostre na tela, como resultado, A correspondente média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa,
o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.
""")

contador = soma = 0
while True:
    nota = int(input('Insira A nota [10, 20]: '))

    if 10 <= nota <= 20:
        pass
    else:
        break
    contador += 1
    soma += nota

print(f'A média é: {soma/contador}.')
