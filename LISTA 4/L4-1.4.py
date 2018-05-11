#coding: utf-8
#Autor: Fernanda Bezerra
vet = []

for i in range (0,10):
    altura = float(input("Digite a altura"))
    vet.append(altura)
media = (sum(vet)/10)
for i in range (0,10):
    if vet [i] > media:
        print ("Altura acima da media", vet [i])
print ("A media é: %.2f ", media)


