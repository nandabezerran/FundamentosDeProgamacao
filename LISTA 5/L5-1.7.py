#coding: utf-8
#Autor: Fernanda Bezerra
#Criando a matriz
mat = {}

#Adicionando valores
for i in range (1,5):

	for j in range (1,5):

		print("Linha: ",i,"Coluna: ",j)
		mat[(i,j)] = int(input())

print ("Elementos da matriz exceto da diagonal principal: ")
d = 4
for i in range (1,5):
	for j in range (1,5):
		if d != j:
			print (mat[(i,j)])
	d -= 1
