#coding: utf-8
#Autor: Fernanda Bezerra
BancoDeOS = []
SomaValores = 0
MaiorValor = 0
cont = 0
Opção = int(input("Deseja utilizar o programa?\n1 - Sim\n2 - Não "))
while Opção == 1:
	DadosOS = {}
	DadosOS['Número'] = int(input("Digite o número da OS: "))
	DadosOS['Data'] = input("Digite a data da OS: ")
	DadosOS['Valor'] = float(input("Digite o valor da OS: "))
	SomaValores += DadosOS['Valor']
	DadosOS['Nome'] = input("Digite o nome do cliente: ")
	BancoDeOS.append(DadosOS)
	if DadosOS['Valor'] > MaiorValor:
		MaiorValor = DadosOS['Valor']
		NomeCliente = DadosOS['Nome']
	cont += 1
	Opção = int(input("Deseja utilizar o programa?\n1 - Sim\n2 - Não "))
MédiaValor = SomaValores/cont
print("A média dos valores das OS: ",MédiaValor,"\nO valor mais caro: ",MaiorValor,"\nNome do cliente: ",NomeCliente)
