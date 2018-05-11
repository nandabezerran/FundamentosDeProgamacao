#coding: utf-8
#Autor: Fernanda Bezerra
Estoque = []
Códigos = []
EstoqueOrdenando = []
for i in range (0,3):
	DadosProduto = {}
	DadosProduto['Código'] = int(input("Digite o código do produto: "))
	DadosProduto['Descrição'] = input("Digite a descrição do produto: ")
	DadosProduto['Valor'] = float(input("Digite o valor do produto: "))
	DadosProduto['Quantidade'] = int(input("Digite a quantidade do produto em estoque: "))
	Estoque.append(DadosProduto)
	Códigos.append(DadosProduto['Código'])
Códigos.sort()

for i in range (0,3):
	for j in Estoque:
		if j['Código'] == Códigos[i]:
			EstoqueOrdenando.append(j.copy())

print("\n", EstoqueOrdenando)