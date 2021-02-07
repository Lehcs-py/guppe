print("""
21. Faça um programa que receba dois números. Calcule e mostre:
    • A soma dos números pares desse intervalo de números, incluindo os números digitados;
    • A multiplicação dos números ímpares desse intervalo, incluindo os digitados;
""")

num1 = int(input('1° número: '))
num2 = int(input('2° Número: '))

soma_par = 0
multiplo_impar = 1
if num1 >= num2:
    for num in range(num2, num1 + 1):
        if num % 2 == 0:
            soma_par += num
        elif num % 2 == 1:
            multiplo_impar *= num
        else:
            pass
    print(f'A soma dos pares no intervalo [{num2}, {num1}] é {soma_par}.')
    print(f'A multiplicação dos impares no intervalo [{num2}, {num1}] é {multiplo_impar}.')

elif num1 < num2:
    for num in range(num1, num2 + 1):
        if num % 2 == 0:
            soma_par += num
        elif num % 2 == 1:
            multiplo_impar *= num
        else:
            pass
    print(f'A soma dos pares no intervalo [{num1}, {num2}] é {soma_par}.')
    print(f'A multiplicação dos impares no intervalo [{num1}, {num2}] é {multiplo_impar}.')

else:
    pass
