#coding: utf-8
#Autor: Fernanda Bezerra
n = int(input("Digite um número menor ou igual a 20 "))
coef = int(input("Digite o coeficiente: "))
soma = 0
x = []

for i in range (0,10):
	x_1 = int(input("Digite um valor: "))
	x.append(x_1)
for j in range (0,10):
	for i in range(n+1, 0,-1):
		soma += coef*x[j]**i
	print ("Valor de X: ",x[j],"Valor de P: ",soma)
