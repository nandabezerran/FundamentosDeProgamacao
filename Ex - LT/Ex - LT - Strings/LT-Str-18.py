#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite uma frase: ")
vetFrase = frase.split(" ")
vetFraseFinal = []

for i in range (0,len(vetFrase)):
	vetFraseFinal.append(vetFrase[i])
	vetFraseFinal.append(vetFrase[i])
fraseFinal = " ".join(vetFraseFinal)
print(fraseFinal)
