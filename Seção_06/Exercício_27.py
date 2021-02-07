print("""
27. Em Matemática, o número harmônico designado por H (n) define-se como sendo A soma da série harmônica:
    H(n) = 1+ 1/2 + 1/3 +1/4 + ... +1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
""")

numero = int(input('Insira n de H(n): '))

soma_harmonica = 0
for num in range(1, numero + 1):
    soma_harmonica += 1/num

print(f'H({numero}) = {soma_harmonica}')
