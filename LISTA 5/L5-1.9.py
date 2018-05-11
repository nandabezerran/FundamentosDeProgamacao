#coding: utf-8
#Autor: Fernanda Bezerra
#Criando a matriz
mat   = {}
mat_1 = {}
C     = {}
for i in range (1,4):

	for j in range (1,3):

		print ("Linha: ",i,"Coluna: ",j)
		mat[(i,j)] = int(input())
for i in range (1,3):

	for j in range (1,6):

		print ("Linha: ",i,"Coluna: ",j)
		mat_1[(i,j)] = int(input())

for i in range (1,4):
	for j in range (1,6):
		C[(i,j)] = 0
		for k in range (1,3):
			C[(i,j)] += mat[(i,k)] * mat_1[(k,j)]

for i in range (1,4):
	for j in range (1,6):
		print (C[(i,j)])