#coding: utf-8
#Autor: Fernanda Bezerra

palavra = input("Digite uma palavra: ")
palavraMinuscula = palavra.lower()
if palavraMinuscula == palavraMinuscula[::-1]:
	print("A palavra",palavra,"é um palíndromo")
else:
	print("A palavra",palavra,"não é um palíndromo")
