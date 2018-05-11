#coding: utf-8
#Autor: Fernanda Bezerra
Palavra = input("Digite uma palavra: ")
Palavra = Palavra.lower()
if Palavra == Palavra[::-1]:
	print("É anagrama")
else:
	print("Não é anagrama")