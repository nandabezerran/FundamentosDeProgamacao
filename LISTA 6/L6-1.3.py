#coding: utf-8
#Autor: Fernanda Bezerra
VetNomeFinal = []
Nome = input("Digite seu nome completo: ")
VetNome = Nome.split()
VetNomeFinal.append(VetNome[len(VetNome) - 1])
VetNomeFinal.append(",")
for i in range (0,len(VetNome)-1):
        VetNomeFinal.append(' ')
        VetNomeFinal.append(VetNome[i])
str1 = ''.join(VetNomeFinal)
print(str1)
