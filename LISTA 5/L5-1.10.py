#coding: utf-8
#Autor: Fernanda Bezerra
#Criando a matriz
mat   = {}
vet_1 = []
vet_2 = []
n     = 1
z     = 1
for i in range (1,4):

	for j in range (1,4):

		print ("Linha: ",i,"Coluna: ",j)
		mat[(i,j)] = int(input())

#Determinante 1 - Diagonal principal 1
d = 1
for i in range (1,4):
	if i == d:
		n*=mat[(i,d)]
		d+=1
vet_1.append(n)

#Determinante 1 - Diagonal principal 2
d = 2
for i in range (1,3):
	z *= mat[(i,d)]
	d + 1
z*=mat[(3,1)]
