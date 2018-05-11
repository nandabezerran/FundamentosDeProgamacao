#coding: utf-8
#Autor: Fernanda Bezerra
vet_1 = []
vet_2 = []
vet_3 = []
vet_4 = [] 
cont = 0
cont_1 = 0
for i in range (0,5):
	n_1=float(input("Digite valor pra o vetor 1: "))
	vet_1.append(n_1)
	n_2=float(input("Digite valor pra o vetor 2: "))
	vet_2.append(n_2)
vet_1.sort()
vet_2.sort()
for i in range (0,5):
	vet_3.append(vet_1[i])
	vet_3.append(vet_2[i])
vet_3.sort()
for i in range (0,10):
        print(vet_3[i])	

