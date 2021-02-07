print("""
29. Escreva um programa para calcular o valor da série, para 5 termos.
    S = 0 + 1/2! + 2/4! +3/6! + ...
""")

numero = 5

soma_e = 0
fatorial = 1
for num in range(1, numero + 1):
    for n in range(1, num + 1):
        fatorial *= (n*2)
    soma_e += num / fatorial

print(f'H({numero}) = {soma_e}')
