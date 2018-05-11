#coding: utf-8
#Autor: Fernanda Bezerra
x = float(input("Digite o valor em graus: "))
vet = []
vet_2 = []
fat = 1
vet_soma = []
y=0
for i in range (1,30,2):
    for j in range (1, i+1):
        fat*=j
    termo = x**i/fat
    vet.append(termo)
    for i in range (1,30,2):
        if i % 2 != 0:
            vet_2.append(termo)
    map(lambda x: x*-1, vet_2)
for i in range (0, 8):
    for j in range (1,16,2):
       vet_soma[j] = vet[j] + vet_2[i]




    
    

        
    
        
        
    
    
