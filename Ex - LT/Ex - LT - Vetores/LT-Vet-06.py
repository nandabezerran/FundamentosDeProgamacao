#coding: utf-8
#Autor: Fernanda Bezerra
vet = []
vet_2 = []
i = 0
vet_aux = []
for i in range (0,10):
	n = float(input("Digite um número: "))
	vet.append(n)
for j in range(0,10):
	while i <= 10:
		if vet[j] > vet[i]:
			vet_aux.append(vet[j])
		else:
			vet_aux.append(vet[i])
		i +=1
	vet_2.append(vet_aux[i])
	i = 0	
for i in range (0,10):
	print(vet_2[i])

