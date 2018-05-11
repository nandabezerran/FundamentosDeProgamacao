#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite uma frase: ")
vetFrase = (frase.split(" "))
cont = 0
palavra = input("Digite a palavra desejada: ")
for i in range (0,len(vetFrase)):
	if palavra == vetFrase[i]:
		cont += 1
print("A quantidade de repetições da palavra",palavra,"é: ", cont)
