#coding: utf-8
#Autor: Fernanda Bezerra

nome = input("Digite o seu nome completo: ")
vetNome = nome.lower().split(" ")
vetUsuario = []
for i in range (0,len(vetNome)):
	if i != len(vetNome)-1:
		aux = vetNome[i]
		vetUsuario.append(aux[0:1])
	else:
		vetUsuario.append(vetNome[len(vetNome)-1])
usuario = "".join(vetUsuario)
print(usuario)