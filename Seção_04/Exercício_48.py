print("""
48. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
""")

segundos = int(input('Insira A quantidade de segundos: '))
horas = segundos / 3600
minutos = segundos / 60
print(f'{horas:.2f} hora(s): {minutos:.2f} minuto(s): {segundos} segundo(s).')
