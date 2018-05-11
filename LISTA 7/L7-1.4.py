#coding: utf-8
#Autor: Fernanda Bezerra
ContasAReceber = []
for i in range(0,15):
	InfoContas = {}
	InfoContas['Número'] = int(input("Digite o número da conta: "))
	InfoContas['Código'] = int(input("Digite o código da conta: "))
	InfoContas['DataVencimento'] = input("Digite a data do vencimento: ")
	InfoContas['DataPagamento'] = input("Digite a data do pagamento")
	InfoContas['Valor'] = float(input("Digite o valor da conta: "))
	if InfoContas['DataPagamento'] > InfoContas['DataVencimento']
		InfoContas['ValorJuros'] = (InfoContas['DataPagamento']-InfoContas['DataVencimento'])*0.02

