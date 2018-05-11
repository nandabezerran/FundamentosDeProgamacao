#coding: utf-8
#Autor: Fernanda Bezerra 
NumeroConta1 = input("Digite o número da primeira conta:\n>>> ")
NumeroConta2 = input("Digite o número da segunda conta:\n>>> ")
NumeroConta3 = input("Digite o número da terceira conta:\n>>> ")
SaldoConta1 = 0
SaldoConta2 = 0
SaldoConta3 = 0

Opção = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Créditar\n2 - Débitar\n3 - Transferência\n4 - Consulta de saldo\n0 - Finalizar programa.\n "))

while Opção != 0:
	if Opção == 1:
		NumeroConta = input("Digite o número da conta que deseja créditar:\n>>> ")
		if NumeroConta == NumeroConta1:
			Valor = float(input("Digite o valor a ser creditado:\n>>> "))
			SaldoConta1 += Valor
		elif NumeroConta == NumeroConta2:
			Valor = float(input("Digite o valor a ser creditado:\n>>> "))
			SaldoConta2 += Valor
		elif NumeroConta == NumeroConta3:
			Valor = float(input("Digite o valor a ser creditado:\n>>>"))
			SaldoConta3 += Valor
		else:
			print("Número da conta incorreto.")
		Opção = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Créditar\n2 - Débitar\n3 - Transferência\n4 - Consulta de saldo\n0 - Finalizar programa.\n "))
	if Opção == 2:
		NumeroConta = input("Digite o número da conta que deseja débitar:\n>>> ")
		if NumeroConta == NumeroConta1:
			Valor = float(input("Digite o valor a ser debitado:\n>>> "))
			SaldoConta1 -= Valor
		elif NumeroConta == NumeroConta2:
			Valor = float(input("Digite o valor a ser debitado:\n>>> "))
			SaldoConta2 -= Valor
		elif NumeroConta == NumeroConta3:
			Valor = float(input("Digite o valor a ser debitado:\n>>> "))
			SaldoConta3 -= Valor
		else:
			print("Número da conta incorreto.")
		Opção = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Créditar\n2 - Débitar\n3 - Transferência\n4 - Consulta de saldo\n0 - Finalizar programa.\n "))
	if Opção == 3:
		NumeroContaDb = input("Digite o número da conta de onde será debitada a transferência:\n>>> ")
		if NumeroContaDb == NumeroConta1:
				Valor = float(input("Digite o valor a ser debitado:\n>>> "))
				SaldoConta1 -= Valor
		elif NumeroContaDb == NumeroConta2:
			Valor = float(input("Digite o valor a ser debitado:\n>>> "))
			SaldoConta2 -= Valor
		elif NumeroContaDb == NumeroConta3:
			Valor = float(input("Digite o valor a ser debitado:\n>>> "))
			SaldoConta3 -= Valor
		else:
			print("Número da conta incorreto.")
		NumeroContaCd = input("Digite o número da conta para onde será tranferido o crédito:\n>>> ")
		if NumeroConta == NumeroConta1:
			SaldoConta1 += Valor
			print("Transferência realizada com sucesso.")
		elif NumeroConta == NumeroConta2:
			SaldoConta2 += Valor
			print("Transferência realizada com sucesso.")
		elif NumeroConta == NumeroConta3:
			SaldoConta3 += Valor
			print("Transferência realizada com sucesso.")
		else:
			print("Número da conta incorreto.")
		Opção = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Créditar\n2 - Débitar\n3 - Transferência\n4 - Consulta de saldo\n0 - Finalizar programa.\n "))
	if Opção == 4:
		NumeroConta = input("Digite o número da conta que deseja visualizar o saldo:\n>>> ")
		if NumeroConta == NumeroConta1:
			print("O saldo atual da conta ",NumeroConta1,"é:\n>>> ",SaldoConta1)
		if NumeroConta == NumeroConta2:
			print("O saldo atual da conta ",NumeroConta2,"é:\n>>> ",SaldoConta2)
		if NumeroConta == NumeroConta3:
			print("O saldo atual da conta ",NumeroConta3,"é:\n>>> ",SaldoConta3)
		Opção = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Créditar\n2 - Débitar\n3 - Transferência\n4 - Consulta de saldo\n0 - Finalizar programa.\n"))
print("O saldo atual da conta ",NumeroConta1,"é:\n>>> ",SaldoConta1)
print("O saldo atual da conta ",NumeroConta2,"é:\n>>> ",SaldoConta2)
print("O saldo atual da conta ",NumeroConta3,"é:\n>>> ",SaldoConta3)