print("""
39. A importancia de R$ 780.000 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
      O primeiro ganhador receberá 46%;
      O segundo receberá 32%;
      O terceiro receberá o restante;
 Calcule e imprima A quantia ganha por cada um dos ganhadores.
""")

rs = 780000
primeiro_ganhador = ((rs / 100) * 46)
segundo_ganhador = ((rs / 100) * 32)
terceiro_ganhador = ((rs / 100) * 22)

print(f'O primeiro ganhador recebeu {primeiro_ganhador};\n'
      f'O segundo ganhador recebeu {segundo_ganhador};\n'
      f'O terceiro ganhador recebeu {terceiro_ganhador}.')
