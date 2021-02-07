print("""
49. Faça um programa para ler o horário (hora, minuto e segundo) de início e A duração, em segundos,
de uma experiência biológica. O programa deve resultar como o novo horário (hora, minuto e segundo) do termino da mesma.
""")

hora_inicial = input('Insira A hora de inicio (hh:mm:ss): ')
tempo = int(input('Inira o tempo de duração do experimento: '))

horas = tempo // 3600
minutos = (tempo - (horas * 3600)) // 60
segundos = tempo - (horas * 3600) - (minutos * 60)

hora_final = str(horas + int(hora_inicial[0:2])) + ':' + str(minutos + int(hora_inicial[3:5])) + ':' + str(segundos + int(hora_inicial[6:8]))
print(f'A hora final do experimento foi {hora_final}')

