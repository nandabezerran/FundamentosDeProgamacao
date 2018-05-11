#coding: utf-8
#Autor: Fernanda Bezerra
n = int(input("Digite a quantidade de candidatos: "))
votos = []
vet = []
op = ""
cont=0
for i in range (0,n):
        nome = input("Qual o nome do candidato? ")
        vet.append(nome)
while op != "fim":
        voto = input()
        for i in range (0,n):
                votos.append(0)
        for i in range (0,n):
                if voto == vet[i]:
                        votos[i]=votos[i] + 1
        op = input("Deseja continuar votando? Senão, escreva fim")
maior=votos[0]
for i in range(0,n):
        if votos[i]> maior:
                maior=vet[i]
                loc_maior = i
        else:
                loc_maior = 0
print (vet[loc_maior])
                





