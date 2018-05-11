#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite uma frase: ")
vogais = "aeiou"

for car in vogais:
	frase = frase.replace(car,"*")
print(frase)
