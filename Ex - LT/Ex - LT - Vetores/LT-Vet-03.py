#coding: utf-8
#Autor: Fernanda Bezerra
vet_1 = []
vet_2 = []
vet_3 = []
for i in range (0,10):
	n_1 = float(input("Digite um número: "))
	n_2 = float(input("Digite um número: "))
	vet_1.append(n_1)
	vet_2.append(n_2)
for i in range (0,10):
	vet_3.append(vet_1[i])
	vet_3.append(vet_2[i])
for i in range (0,20):
	print (vet_3[i])
