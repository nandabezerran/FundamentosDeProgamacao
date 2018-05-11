#coding: utf-8
#Autor: Fernanda Bezerra
#Criando a matriz
mat = {}

#Adicionando valores
for i in range (1,5):

	for j in range (1,5):

		print("Linha: ",i,"Coluna: ",j)
		mat[(i,j)] = int(input())

print ("Diagonal principal")
d = 1
for k in range (1,5):
	print (mat[(k,d)])
	d += 1



