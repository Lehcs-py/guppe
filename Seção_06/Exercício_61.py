print("""
61. Faça um programa que calcule o maior número palíndromo feito A partir do produto de dois números de 3 dígitos. 
Ex: O maior palíndromo feito A partir do produto de dois números de dois dígitos é 9009 = 91 * 99.
""")

contador = maior = v_num1 = v_num2 = 0
for num1 in range(1000):
    for num2 in range(1000):
        if len(str(num1)) == 3 and len(str(num2)) == 3:
            palindromo = (num2 * num1)

            if str(palindromo) == str(palindromo)[::-1]:
                contador += 1

                if contador == 1:
                    maior = palindromo
                else:
                    if palindromo >= maior:
                        maior = palindromo
                        v_num1 = num1
                        v_num2 = num2
            else:
                pass

        else:
            pass

print(f'{maior} = {v_num1} * {v_num2}')
