#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite uma frase: ")
print(" ".join([word[::-1] for word in frase.split()]))
