#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite uma frase: ")
vetFrase = (frase.split(" "))
cont = 0
for i in range (0,len(vetFrase)):
	if vetFrase[i] == "aula" or vetFrase[i] == "Aula" or vetFrase[i] == "AULA":
		cont += 1
print(cont)
