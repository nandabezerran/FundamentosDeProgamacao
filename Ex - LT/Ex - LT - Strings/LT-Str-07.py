#coding: utf-8
#Autor: Fernanda Bezerra

frase = input("Digite a primeira frase: ")
vetFrase = (frase.split(" "))
fraseOrdenada = " ".join(sorted(vetFrase))
print(fraseOrdenada)
