print("""
44. Receba A Altura do degrau de uma escada e A Altura que o usuário deseja alcançar subindo A escada.
Calcule e mostre quantos degraus o usuário devera subir para atingir seu objetivo.
""")

altura_do_degrau = float(input('Insira A altura do degrau: '))
altura_desejada = float(input('Insira A altura desejada: '))
degraus = altura_desejada / altura_do_degrau

print(f'O usuário devera subir {int(degraus)} degraus.')
