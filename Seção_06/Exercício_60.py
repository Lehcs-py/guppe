print("""
60. Faça um programa que leia vários números, calcule e mostre:
    (A) A soma dos números digitados
    (B) A quantidade de números digitados
    (c) A média dos números digitados
    (d) O maior número digitado
    (e) O menor número digitado
    (f) A média dos números pares
Finalize A entrada de dados caso o usuário informe o valor 0.
""")

numero = 1
contador = maior = menor = soma = soma_par = contador_par = 0
while True:
    numero = int(input(f'Insira o {contador + 1}° número: '))

    if numero != 0:
        contador += 1
    else:
        break

    soma += numero

    if numero % 2:
        soma_par += numero
        contador_par += 1
    else:
        pass

    if contador == 1:
        maior = menor = numero
    else:
        if numero >= maior:
            maior = numero

        elif numero <= menor:
            menor = numero

print(f"""
A soma dos números digitados: {soma}
A quantidade de números digitados: {contador}
A média dos números digitados: {soma / contador}
O maior número digitado: {maior}
O menor número digitado: {menor}
A média dos números pares: {soma_par / contador_par}
""")
