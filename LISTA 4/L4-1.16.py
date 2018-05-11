#coding:utf-8
#Autor: Fernanda Bezerra
n = int(input("Digite a quantidade de alunos na sala: "))
cartao_gab = []
vet_alunos = []
vet_mostrar = []
cont = 0
for i in range (0,3):
	resp = input("Digite a resposta da questão ")
	cartao_gab.append(resp)
for i in range (0,n):
	vet_resp = []
	vet = []
	for j in range (0,3):
		opc = input("Digite a resposta do aluno para questao ")
		vet_resp.append(opc)
	for z in range (0,3):
		if vet_resp[z] == cartao_gab[z]:
			cont += 1
	num = int(input("Digite o número do aluno"))
	vet.append(cont)
	vet.append(num)
	vet_mostrar.append(vet)
	cont = 0
for i in range (0,n):
	print (vet)


	

