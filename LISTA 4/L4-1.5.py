# coding: utf-8
# Autor: Fernanda Bezerra
f1 = 1
f2 = 2
vet = []
vet.append(f1)
vet.append(f2)
for i in range(2,50):
    f3 = f1 + f2
    vet.append(f3)
    f1 = f2
    f2 = f3
for i in range (0,50):
    print (vet[i])
