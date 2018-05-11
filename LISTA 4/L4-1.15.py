#coding: utf-8
#Autor: Fernanda Bezerra
vet = []
n = int(input("Digite a quantidade de números que deseja fornecer: "))
soma = 0
for i in range(0,n):
	num = float(input("Digite o número: "))
	vet.append(num)
media = sum(vet)/n
for i in range (0,n):
	soma+=(vet[i]-media)**2
variancia = soma/(n-1)
dp = variancia**1/2
print("Media: ",media,"Variancia: ",variancia,"Desvio padrão",dp)