#coding: utf-8
#Autor: Fernanda

Mat = []
Vet = []
VetSoma = []
Soma = 0

for i in range(0,2):
	for j in range(0,3):
		Vet.append(int(input()))
	Mat.append(Vet)
	Vet = []
for i in range(0,2):
	for j in range(0,3):
		Soma += Mat[i][j]
	VetSoma.append(Soma)
for i in range (0,2):
	for j in range(0,3):
		aux = Mat[i][j] * sum(VetSoma)
		Mat[i][j] = aux
print(Mat)
