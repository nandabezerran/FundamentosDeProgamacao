#coding: utf-8
#Autor: Fernanda Bezerra
Senha = input("Digite uma senha: ")
if len(Senha) < 8 or len(Senha) > 15:
	print("Quantidade inválida de carácteres")
elif Senha.isupper() == True:
	print("Deve haver pelo menos um caractere minusculo.")
elif Senha.islower() == True:
	print("Deve haver pelo menos um caractere maiusculo.")
else:
	print("Senha válida")