print("""
20. Leia um valor de massa em Quilogramas e apresente-o convertido em Libras.
A fórmula  de conversão é: L = K/0.45, sendo K A massa em quilogramas e L A massa em libras.
""")

quilograma = float(input('Insira o valor da massa em Quilogramas para A conversão em Libras: '))
libra = quilograma / 0.45
print(input(f'{quilograma} kg = {libra} lb.'))
