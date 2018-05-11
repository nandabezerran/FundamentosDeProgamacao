#coding: utf-8
#Autor: Fernanda Bezerra
#Criando a matriz
mat = {}
vet = []
aux = 0
#Adicionando valores
for i in range (1,4):

	for j in range (1,6):

		print ("Linha: ",i,"Coluna: ",j)
		mat[(i,j)] = int(input())

for k in range (0,3):
	
	for i in range (1,4):

		for j in range (1,6):

			aux += mat[(i,j)]
		vet.append(aux)
		aux = 0
for z in range (0,3):
	print (vet[z])
