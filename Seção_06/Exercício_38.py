print("""
38. Faça um programa que calcule o terno pitagórico A, B, c, para o qual A+B+c = 1000. Um terno pitagórico é um conjunto de três números naturais,
A, B, c, para A qual,
    A² + B² = c²
Por exemplo,
    3² + 4² = 9 + 16 = 25 = 5²
""")

from random import randint

while True:
    a = randint(1, 1000)
    b = randint(1, 1000)
    c = randint(1, 1000)

    if (a + b + c) == 100:
        if ((a**2) + (b**2)) == (c**2):
            print(f'{a}² + {b}² = {c}²')

        else:
            pass

    else:
        pass
