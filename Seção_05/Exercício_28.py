print("""
28. Faça um programa que leia três números inteiros positivos
e efetue o cálculo de uma das seguintes médias de acrodo com
um valor numérico digitado pelo usuário:
    (A) Geométrica: 3√x*y*z
    (B) Ponderada: ((x*2)+(y*3)+(z*1))/6
    (c) Harmônica: 1/((1/x)+(1/y)+(1/z))
    (d) Aritmética: (x+y+z)/3
""")

x = int(input('Insira o 1° número: '))
y = int(input('Insira o 2° número: '))
z = int(input('Insira o 3° número: '))

geometrica = (x*y*z)**(1/3)
ponderada = ((x*2)+(y*3)+(z*1))/6
harmonica = 1/((1/x)+(1/y)+(1/z))
aritmetica = (x+y+z)/3

print(f'''
Geométrica: ∛{x}*{y}*{z} = {geometrica}

Ponderada: (({x}*2)+({y}*3)+({z}*1))/6 = {ponderada}

Harmônica: 1/((1/{x})+(1/{y})+(1/{z})) = {harmonica}

Aritmética: ({x}+{y}+{z})/3 = {aritmetica}
''')
