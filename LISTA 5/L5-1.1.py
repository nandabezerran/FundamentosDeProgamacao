#coding: utf-8
#Autor: Fernanda Bezerra
mat = [[],[],[],[],[],[]]
for i in range (0,6):
	for j in range (0,3):
		n = int(input("Digite o número: "))
		mat[i].append(n)
maior=mat[0][0]
menor=mat[0][0]
for i in range (0,6):
	for j in range (0,3):
				if mat[i][j]>maior:
					maior=mat[i][j]
				if mat[i][j]<menor:
					menor=mat[i][j]
print(maior,menor)
for i in range (0,6):
	for j in range (0,3):
		print(mat[i][j])
