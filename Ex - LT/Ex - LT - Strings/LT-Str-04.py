#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite a frase: ")
vetCont = [0,len(frase)]
contAux = 0
for i in range (0,len(frase)):
	for j in range (0,len(frase)-1):
		if frase[i] == frase[j+1] and frase[i] != " " and frase[j+1] != " ":
			contAux += 1
			letra = frase[i]
	if contAux >= 1:
		print("Letra: ",letra,"Repetições: ",contAux)
	contAux = 0

