print("""
21. Leia um valor de massa em Libras e apresente-o convertido em Quilogramas.
A fórmula de conversão é: K = L*0.45, sendo K A massa em quilogramas e L A massa em libras.
""")

libra = float(input('Insira o valor da massa em Libras para A conversão em Quilogramas: '))
quilograma = libra * 0.45
print(f'{libra} lb = {quilograma} kg.')
