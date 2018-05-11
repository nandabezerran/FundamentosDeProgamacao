#coding: utf-8
#Autor: Fernanda Bezerra
VetBanco = []
Aux = []
NumeroContas = int(input("Digite a quantidade de contas:\n>>> "))
for i in range (0,NumeroContas):
	Banco = {}
	Banco['Numero'] = int(input("Digite o número da conta:\n>>> "))
	Banco['Saldo'] = float(input("Digite o saldo da conta:\n>>> "))
	VetBanco.append(Banco)
Opc = int(input("### Menu de opções ###\n1-Créditar\n2-Débitar\n3-Transferir\n4-Consulta de saldo\n0-Encerrar programa\n>>> "))
print(VetBanco)
while Opc != 0:
	if Opc == 1:
		print("### Créditar ###")
		NumeroConta = int(input("Digite o número da conta que deseja creditar: "))
		for Banco in VetBanco:
			if NumeroConta == Banco['Numero']:
				ValorCredito = float(input("Digite o valor do crédito:\n>>> "))
				Banco['Saldo'] += ValorCredito
				print(Banco['Numero'])
				print(Banco['Saldo'])
		Opc = int(input("### Menu de opções ###\n1-Créditar\n2-Débitar\n3-Transferir\n4-Consulta de saldo\n0-Encerrar programa\n>>> "))
	if Opc == 2:
		print("### Débitar ###")
		NumeroConta = int(input("Digite o número da conta que deseja débitar: "))
		for Banco in VetBanco:
			if NumeroConta == Banco['Numero']:
				ValorDébito = float(input("Digite o valor do débito:\n>>> "))
				Banco['Saldo'] -= ValorDébito
				print(Banco['Numero'])
				print(Banco['Saldo'])
		Opc = int(input("### Menu de opções ###\n1-Créditar\n2-Débitar\n3-Transferir\n4-Consulta de saldo\n0-Encerrar programa\n>>> "))
	if Opc == 3:
		print("### Transferência ###")
		NumeroConta1 = int(input("Digite o número da conta que deseja debitar: "))
		NumeroConta2 = int(input("Digite o número da conta que deseja creditar: "))
		ValorTrans = float(input("Digite o valor da transferência"))
		for Banco in VetBanco:
			if NumeroConta1 == Banco['Numero']:
				Banco['Saldo'] -= ValorTrans
				print(Banco['Numero'])
				print(Banco['Saldo'])
		for Banco in VetBanco:
			if NumeroConta 2== Banco['Numero']:
				Banco['Saldo'] += ValorTrans
				print(Banco['Numero'])
				print(Banco['Saldo'])
	if Opc == 4:
		print("### Consulta de Saldo ###")
		NumeroConta = int(input("Digite o numero da conta que deseja visualizar o saldo:"))
		for Banco in VetBanco:
			if NumeroConta1 == Banco['Numero']:
				print(Banco['Numero'])
				print(Banco['Saldo'])