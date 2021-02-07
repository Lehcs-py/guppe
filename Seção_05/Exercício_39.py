print("""
39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e o
tempo de serviço de cada funcionário. Os funcionário com menores salários terão um aumento proporcionalmente maior do
que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
adicional de salário.Faça um programa que leia:
    O valor do salário atual do funcionário;
    O tempo de serviço desse funcionário na empresa (número de anos trabalhados na empresa).


	Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma
	mensagem caso o funcionário não tenha direito A nenhum aumento.

	      Salário Atual   |     Reajuste(%)    |  Tempo de Serviço |   Bônus
	      Até 500.00      |         25%        |  Abaixo de 1 ano  | Sem bônus
	      Até 1000.00     |         20%        |  De 1 A 3 anos    |  100.00
	      Até 1500.00     |         15%        |  De 4 A 6 anos    |  200.00
	      Até 2000.00     |         10%        |  De 7 A 10 anos   |  300.00
          Acima de 2000.00|    Sem reajuste    |  Mais de 10 anos  |  500.00
""")

salario_atual = int(input('Insira o salário atual: R$'))
tempo_servico = int(input('Insira o tempo de servico: '))

salario_novo = float
if 0 <= salario_atual <= 500:
    salario_novo = salario_atual + ((salario_atual / 100) * 25)

elif 500 < salario_atual <= 1000:
    salario_novo = salario_atual + ((salario_atual / 100) * 20)

elif 1000 < salario_atual <= 1500:
    salario_novo = salario_atual + ((salario_atual / 100) * 15)

elif 1500 < salario_atual <= 2000:
    salario_novo = salario_atual + ((salario_atual / 100) * 10)
else:
    salario_novo = salario_atual

bonus = int
if tempo_servico < 1:
    bonus = 0
elif 1 <= tempo_servico <= 3:
    bonus = 100
elif 4 <= tempo_servico <= 6:
    bonus = 200
elif 7 <= tempo_servico <= 10:
    bonus = 300
elif 10 < tempo_servico:
    bonus = 500
else:
    bonus = 0

print(f'Novo salário: R${salario_novo + bonus}')
