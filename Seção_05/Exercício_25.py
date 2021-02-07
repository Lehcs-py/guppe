print("""
25. Calcule as raízes da equação de 2° grau.
Lembrando que x = (-B ± √∆)/2a onde ∆ = B² - 4ac e ax² + bx + c = 0 representa uma equação de 2° grau.
A variável A tem que ser diferente de zero. Caso seja igual, imprima A mensagem "Não é equação do segundo grau".
    Se ∆ < 0, não existe real. Imprima A mensagem Não existe raiz.
    Se ∆ = 0, existe uma raiz real. Imprima A raiz e A mensagem Raiz única.
    Se ∆ >= 0, imprima as duas raízes reais.
""")

print('Para calcular A equação de 2° grau, insira: ')
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

delta = ((b**2) - (4*a*c))

x1 = ((b*(-1)) + (delta**0.5))/(2*a)
x2 = ((b*(-1)) - (delta**0.5))/(2*a)

if a == 0:
    print('Não é uma equção do 2° grau.')

elif delta < 0:
    print('Não existe raiz')

elif delta == 0:
    print(f'Raiz única: {x1}')

elif delta > 0:
    print(f'Raizes: ({x1}, {x2})')
