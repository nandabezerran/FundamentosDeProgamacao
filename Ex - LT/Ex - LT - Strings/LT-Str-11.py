#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite uma frase: ")
vetFrase = (frase.split(" "))
for i in range (0,len(vetFrase)):
	if vetFrase[i] == "teclado":
		vetFrase[i] = "teclado ou mouse"
fraseMudada = " ".join(vetFrase)
print(fraseMudada)