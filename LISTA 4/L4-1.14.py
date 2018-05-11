#coding: utf-8
#Autor: Fernanda Bezerra
altura = []
sexo = []
nome = []
for i in range(0,4):
	a = float(input("Digite sua altura: "))
	s = int(input("Digite seu sexo: 1-Masculino 2-Feminino"))
	n = input("Digite seu nome: ")
for i in range(0,4):
	for j in range (0,2):
		if altura[i] > altura[j+1]:
			altura[i]=altura[j+1]
x=altura

