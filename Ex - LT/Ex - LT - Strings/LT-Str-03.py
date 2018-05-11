#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite uma frase: ")
contEspaços = 0
for i in range(0,len(frase)):
	if frase[i] == " ":
		contEspaços += 1
contEspaços +=1
print(contEspaços)
