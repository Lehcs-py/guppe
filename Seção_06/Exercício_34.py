print("""
34. Faça um programa que calcule o menor número divisível por cada um dos números de 1 A 20?
Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 A 10, sem sobrar resto.
""")

contador = num = 0
while contador != 1:
    num += 1

    if (num % 1 == 0 and num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0
            and num % 6 == 0 and num % 7 == 0 and num % 8 == 0 and num % 9 == 0 and num % 10 == 0
            and num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and num % 14 == 0 and num % 15 == 0
            and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0):
        print(num)
        break

    else:
        pass
