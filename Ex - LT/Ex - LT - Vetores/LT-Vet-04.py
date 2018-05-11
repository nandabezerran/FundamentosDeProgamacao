#coding: utf-8
#Autor: Fernanda Bezerra
vet = []
vet_p = []
vet_n = []
contP=0
contN=0
for i in range (0,8):
	n = float(input("Digite um número: "))
	vet.append(n)
for i in range(0,8):
	if vet[i] >= 0:
		vet_p.append(vet[i])
		contP+=1
	else:
		vet_n.append(vet[i])
		contN+=1
if contN == 0 and contP != 0:
	print("Não há números negativos")
elif contP == 0:
	print("Não há números positivos")
for i in range (0,contP):
	print ("Positivos"vet_p[i])
for i in range (0,contN):
	print ("Negativos"vet_n[i])
