#coding: utf-8
#Autor: Fernanda Bezerra
BancoDeDados = []
SomaSalário = 0
SomaFilhos = 0
MaiorSalário = 0
ContMulheres = 0
for i in range (0,20):
	Dados = {}
	Dados['Salário'] = float(input("Digite o seu salário: "))	
	SomaSalário += Dados['Salário']
	Dados['Idade'] = int(input("Digite a sua idade: "))
	Dados['Sexo'] = int(input("Digite seu sexo\n1 - Para masculino\n2 - Para feminino"))
	Dados['Número de filhos'] = int(input("Digite a quantidade de filhos que possui: "))
	SomaFilhos += Dados['Número de filhos']
	BancoDeDados.append(Dados)
	if Dados['Sexo'] == 2 and Dados['Salário'] > 10.000:
		ContMulheres += 1
	if Dados['Salário'] > MaiorSalário:
		MaiorSalário = Dados['Salário']
MédiaSalário = SomaSalário/20
MédiaFilhos = SomaFilhos/20
print("A média dos salários é: ",MédiaSalário,"\nA média de filhos é: ",MédiaFilhos,"\n O maior salário é: ",MaiorSalário,"\nQuantidade de mulheres que recebem mais que 10.000 é: ",ContMulheres)
