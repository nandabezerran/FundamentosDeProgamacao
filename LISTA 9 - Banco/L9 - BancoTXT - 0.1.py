#coding: utf-8
#Autor: Fernanda Bezerra
import os
Arquivo = open('Banco.txt', 'a')
Arquivo.close()
AchouConta = 0
Opc = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Criar conta\n2 - Remover conta\n3 - Créditar\n4 - Débitar\n5 - Transferência\n6 - Consulta de saldo\n0 - Finalizar programa.\n>>> "))

while Opc != 0:
	if Opc == 1:
		print("### Criar conta ###")
		NumeroConta = input("Digite o número da conta:\n>>> ")
		Arquivo = open('Banco.txt')
		AchouConta = 0
		#Verificar se a conta existe
		for linha in Arquivo:
			Dados = linha.split()
			Conta = {}
			Conta['Numero'] = Dados[0]
			Conta['Saldo'] = float(Dados[1])
			if Conta ['Numero'] == NumeroConta:
				AchouConta += 1
				print("Conta já existente.")
		if AchouConta == 0:
			Conta = {}	
			SaldoConta = float(input("Digite o saldo da conta:\n>>> "))
			Conta['Numero'] = NumeroConta
			Conta['Saldo'] = SaldoConta
			Arquivo.close()
			Arquivo = open('Banco.txt', 'a')
			linha = "{0} {1}\n".format(Conta['Numero'],Conta['Saldo'])
			Arquivo.write(linha)
			Arquivo.close()
			print("\n>>> Conta criada com sucesso.")
		Opc = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Criar conta\n2 - Remover conta\n3 - Créditar\n4 - Débitar\n5 - Transferência\n6 - Consulta de saldo\n0 - Finalizar programa.\n>>> "))
	if Opc == 2:
		print("### Remover conta ###")
		NumeroConta = input("Digite o número da conta:\n>>> ")
		Arquivo = open('Banco.txt','r')
		#Verificar se a conta existe
		AchouConta = 0
		for linha in Arquivo:
			Dados = linha.split()
			Conta = {}
			Conta['Numero'] = Dados[0]
			Conta['Saldo'] = float(Dados[1])
			if Conta ['Numero'] == NumeroConta:
				AchouConta +=1
		if AchouConta == 0:
			print(">>> Conta não existe. Tente novamente.")
		Arquivo.close()
		if AchouConta != 0:
			Arquivo = open('Banco.txt','r')
			Arquivo_tmp = open('Banco_tmp.txt','w')
			for linha in Arquivo:
				Dados = linha.split()
				Conta = {}
				Conta['Numero'] = Dados[0]
				Conta['Saldo'] = float(Dados[1])
				if Conta['Numero'] != NumeroConta:
					Arquivo_tmp.write(linha)
			Arquivo.close()
			Arquivo_tmp.close()
			os.remove('Banco.txt')
			os.rename('Banco_tmp.txt','Banco.txt')
			print(">>> Operação efetuada com sucesso.")
		Opc = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Criar conta\n2 - Remover conta\n3 - Créditar\n4 - Débitar\n5 - Transferência\n6 - Consulta de saldo\n0 - Finalizar programa.\n>>> "))
	if Opc == 3:
		print("### Creditar ###")
		NumeroConta = input("Digite o número da conta:\n>>> ")
		Arquivo = open('Banco.txt','r')
		#Verificar se a conta existe
		AchouConta = 0
		for linha in Arquivo:
			Dados = linha.split()
			Conta = {}
			Conta['Numero'] = Dados[0]
			Conta['Saldo'] = float(Dados[1])
			if Conta ['Numero'] == NumeroConta:
				AchouConta = 1
		if AchouConta == 0:
			print(">>> Conta não existe. Tente novamente.")
		Arquivo.close()
		if AchouConta != 0:
			ValorCredito = float(input("Digite o valor que deseja creditar:\n>>> "))
			Arquivo = open('Banco.txt','r')
			Arquivo_tmp = open('Banco_tmp.txt', 'w')
			for linha in Arquivo:
				Dados = linha.split()
				Conta['Numero'] = Dados[0]
				Conta['Saldo'] = float(Dados[1])
				if Conta['Numero'] != NumeroConta:
					Arquivo_tmp.write(linha)
				else:
					Conta['Saldo'] += ValorCredito
					linha = "{0} {1}\n".format(Conta['Numero'],Conta['Saldo'])
					Arquivo_tmp.write(linha)
			Arquivo.close()
			Arquivo_tmp.close()
			os.remove('Banco.txt')
			os.rename('Banco_tmp.txt','Banco.txt')
			print(">>> Operação efetuada com sucesso.")
		Opc = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Criar conta\n2 - Remover conta\n3 - Créditar\n4 - Débitar\n5 - Transferência\n6 - Consulta de saldo\n0 - Finalizar programa.\n>>> "))
	if Opc == 4:
		print("### Debitar ###")
		NumeroConta = input("Digite o número da conta:\n>>> ")
		Arquivo = open('Banco.txt','r')
		#Verificar se a conta existe
		AchouConta = 0
		for linha in Arquivo:
			Dados = linha.split()
			Conta = {}
			Conta['Numero'] = Dados[0]
			Conta['Saldo'] = float(Dados[1])
			if Conta ['Numero'] == NumeroConta:
				AchouConta = 1
		if AchouConta == 0:
			print(">>> Conta não existe. Tente novamente.")
		Arquivo.close()
		if AchouConta != 0:
			ValorCredito = float(input("Digite o valor que deseja debitar:\n>>> "))
			Arquivo = open('Banco.txt','r')
			Arquivo_tmp = open('Banco_tmp.txt', 'w')
			for linha in Arquivo:
				Dados = linha.split()
				Conta['Numero'] = Dados[0]
				Conta['Saldo'] = float(Dados[1])
				if Conta['Numero'] != NumeroConta:
					Arquivo_tmp.write(linha)
				else:
					Conta['Saldo'] -= ValorCredito
					linha = "{0} {1}\n".format(Conta['Numero'],Conta['Saldo'])
					Arquivo_tmp.write(linha)
			Arquivo.close()
			Arquivo_tmp.close()
			os.remove('Banco.txt')
			os.rename('Banco_tmp.txt','Banco.txt')
			print(">>> Operação efetuada com sucesso.")
		Opc = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Criar conta\n2 - Remover conta\n3 - Créditar\n4 - Débitar\n5 - Transferência\n6 - Consulta de saldo\n0 - Finalizar programa.\n>>> "))
	if Opc == 5:
		print("### Transferir ###")
		NumeroConta = input("Digite o número da conta de onde será debitada a tranferência:\n>>> ")
		Arquivo = open('Banco.txt','r')
		#Verificar se a conta existe
		AchouConta = 0
		for linha in Arquivo:
			Dados = linha.split()
			Conta = {}
			Conta['Numero'] = Dados[0]
			Conta['Saldo'] = float(Dados[1])
			if Conta ['Numero'] == NumeroConta:
				AchouConta += 1
		if AchouConta == 0:
			print(">>> Conta não existe. Tente novamente.")
		Arquivo.close()
		NumeroConta1 = input("Digite o número da conta de onde será creditada a transferência:\n>>> ")
		Arquivo = open('Banco.txt','r')
		#Verificar se a conta existe
		AchouConta1 = 0
		for linha in Arquivo:
			Dados = linha.split()
			Conta = {}
			Conta['Numero'] = Dados[0]
			Conta['Saldo'] = float(Dados[1])
			if Conta ['Numero'] == NumeroConta:
				AchouConta1 += 1
		if AchouConta1 == 0:
			print(">>> Conta não existe. Tente novamente.")
		Arquivo.close()
		if AchouConta != 0 and AchouConta1 != 0:
			ValorTrans = float(input("Digite o valor que deseja transferir:\n>>> "))
			Arquivo = open('Banco.txt','r')
			Arquivo_tmp = open('Banco_tmp.txt', 'w')
			for linha in Arquivo:
				Dados = linha.split()
				Conta = {}
				Conta['Numero'] = Dados[0]
				Conta['Saldo'] = float(Dados[1])
				if Conta['Numero'] != NumeroConta:
					Arquivo_tmp.write(linha)
				else:
					Conta['Saldo'] -= ValorTrans
					linha = "{0} {1}\n".format(Conta['Numero'],Conta['Saldo'])
					Arquivo_tmp.write(linha)
			Arquivo.close()
			Arquivo_tmp.close()
			os.remove('Banco.txt')
			os.rename('Banco_tmp.txt','Banco.txt')
			Arquivo = open('Banco.txt','r')
			Arquivo_tmp = open('Banco_tmp.txt', 'w')
			for linha in Arquivo:
				Conta = {}
				Dados = linha.split()
				Conta['Numero'] = Dados[0]
				Conta['Saldo'] = float(Dados[1])
				if Conta['Numero'] != NumeroConta1:
					Arquivo_tmp.write(linha)
				else:
					Conta['Saldo'] += ValorTrans
					linha = "{0} {1}\n".format(Conta['Numero'],Conta['Saldo'])
					Arquivo_tmp.write(linha)
			Arquivo.close()
			Arquivo_tmp.close()
			os.remove('Banco.txt')
			os.rename('Banco_tmp.txt','Banco.txt')
			print(">>> Operação efetuada com sucesso.")
		Opc = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Criar conta\n2 - Remover conta\n3 - Créditar\n4 - Débitar\n5 - Transferência\n6 - Consulta de saldo\n0 - Finalizar programa.\n>>> "))
	if Opc == 6:
		print("### Consulta de saldo ###")
		NumeroConta = input("Digite o número da conta que deseja visualizar o saldo:\n>>> ")
		Arquivo = open('Banco.txt','r')
		#Verificar se a conta existe
		AchouConta = 0
		for linha in Arquivo:
			Dados = linha.split()
			Conta = {}
			Conta['Numero'] = Dados[0]
			Conta['Saldo'] = float(Dados[1])
			if Conta ['Numero'] == NumeroConta:
				AchouConta += 1
		if AchouConta == 0:
			print(">>> Conta não existe. Tente novamente.")
		Arquivo.close()
		if AchouConta != 0:
			Arquivo = open('Banco.txt','r')
			for linha in Arquivo:
				Conta = {}
				Dados = linha.split()
				Conta['Numero'] = Dados[0]
				Conta['Saldo'] = float(Dados[1])
				if Conta['Numero'] == NumeroConta:
					linha = Conta['Saldo']
					print (linha)
			Arquivo.close()
		Opc = int(input("### MENU DE OPÇÕES ###\nDigite a opção:\n1 - Criar conta\n2 - Remover conta\n3 - Créditar\n4 - Débitar\n5 - Transferência\n6 - Consulta de saldo\n0 - Finalizar programa.\n>>> "))
	if Opc == 0:
		print("Programa encerrado.")	