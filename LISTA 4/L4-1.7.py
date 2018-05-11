#coding: utf-8
#Autor: Fernanda Bezerra
vet = []
cont = 0
for i in range (0,121):
    temp = float(input("Digite a temperatura: "))
    if 15 <= temp and temp <= 40:
        vet.append(temp)
    else:
        print ("Temperatura inválida")
media = sum(vet)/len(vet)
menor = vet[0]
maior = vet [0]
for i in range (0,121):
    if vet[i] > maior:
        maior = vet[i]
    if vet[i] < menor:
        menor = vet [i]
    if vet [i] < media:
        cont+=1
print ("A maior temperatura: ", maior, "a menor temperatura: ", menor,"quantidade de temperaturas menores que a media",cont)
    
