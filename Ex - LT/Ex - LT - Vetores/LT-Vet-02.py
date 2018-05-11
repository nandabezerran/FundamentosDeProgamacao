#coding: utf-8
#Autor: Fernanda Bezerra
vet_vu = []
vet_qnt = []
vet_vt = []
cont_ov = 0
for i in range(0,3):
	vu = float(input("Digite o valor unitário do produto:"))
	qnt = int(input("Digite a quantidade vendida do produto:"))
	vt = vu*qnt
	vet_vu.append(vu)
	vet_qnt.append(qnt)
	vet_vt.append(vt)
	vt = 0
for i in range(0,3):
	if vet_qnt[i] > cont_ov:
		cont_ov = i
for i in range(0,3):
	print("Quantidade vendida:",vet_qnt[i],"Valor unitário:",vet_vu[i],"Valor total:",vet_vt[i])
print("Valor total das vendas:",sum(vet_vt), "Valor da comissão:",sum(vet_vt)*0.05,"Objeto mais vendido:",cont_ov)
