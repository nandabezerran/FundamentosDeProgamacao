#coding: utf-8
#Autor: Fernanda Bezerra

frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")
vetFinal = []
vetFrase1 = (frase1.split(" "))
vetFrase2 = (frase2.split(" "))
h = 0
z = 0
for i in range (0,len(vetFrase1)+len(vetFrase2)):
	if i % 2 == 0:
		vetFinal.append(vetFrase1[h])
		h += 1
	else:
		vetFinal.append(vetFrase2[z])
		z += 1
string = " ".join(vetFinal)
print(string)
