#coding: utf-8
#Autor: Fernanda Bezerra
n = int(input("Digite a quantidade de elementos: "))
x = []
y = []
vet = []
for i in range (0,n):
	num = float(input("Digite um número: "))
	x.append(num)
	num1 = float(input("Digite um número: "))
	y.append(num1)
for j in range (0,n):
	vet.append(x[j]*y[j])
print(vet)


