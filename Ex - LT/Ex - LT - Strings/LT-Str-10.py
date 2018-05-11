#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite uma frase: ")
vetFrase = (frase.split(" "))

for i in range (0, len(vetFrase)):
	if vetFrase[i] == "aluno" or vetFrase[i] == "Aluno" or vetFrase[i] == "ALUNO":
		vetFrase[i] = "estudante"
	elif vetFrase[i] == "escola" or vetFrase[i] == "Escola" or vetFrase[i] == "ESCOLA":
		vetFrase[i] = "universidade"
fraseMudada = " ".join(vetFrase)
print(fraseMudada)
