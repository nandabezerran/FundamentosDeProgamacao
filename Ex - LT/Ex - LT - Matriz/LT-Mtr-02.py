#coding: utf-8
#Autor: Fernanda Bezerra

Mat = []
Vet = []
cont1 = 0
cont2 = 0
cont3 = 0
for i in range(0,2):
	for j in range(0,3):
		print("Digite a nota",j,"do usuário",i)
		Vet.append(float(input()))
	Mat.append(Vet)
	Vet = []
for i in range(0,2):
	Menor = Mat[i][0]
	for j in range(0,3):
		Atual = Mat[i][j]
		if Atual < Menor :
			Menor = Atual
	print("Aluno:",i,"menor nota:",Menor)
	for j in range(0,3):
		if Menor == Mat[i][0]:
			cont1+=1
		elif Menor == Mat[i][1]:
			cont2+=1
		elif Menor == Mat[i][2]:
			cont3+=1
print(cont1,cont2,cont3)
	
