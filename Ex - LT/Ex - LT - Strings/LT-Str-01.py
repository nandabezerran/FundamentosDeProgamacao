#coding: utf-8
#Autor: Fernanda Bezerra
frase = input("Digite uma frase: ")
vet = ['A','E','I','O','U','a','e','i','o','u']
contVogais = 0
for i in range(0,len(frase)):
        for j in range (0,10):
                if frase[i] == vet[j]:
                        contVogais += 1
print(contVogais)
