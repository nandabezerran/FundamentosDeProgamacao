#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite uma frase: ")
vetFrase = frase.split(" ")
palavra = input("Digite a palavra: ")
for i in range (0,len(vetFrase)):
	if vetFrase[i] == "escola" or vetFrase[i] == "Escola":
		vetFrase[i] = palavra
fraseAlterada = " ".join(vetFrase)
print(fraseAlterada)
