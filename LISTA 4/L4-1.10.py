#coding; utf-8
#Autor: Fernanda Bezerra
vet = []
for j in range (1,5):
    for i in range (1,4):
        valor = float(input("Digite o valor da mercadoria: "))
        qnt_vendas = float(input("Digite a quntidade de vendas: "))
        fatura = valor*qnt_vendas
        vet.append(fatura)
        print("Dia",j,"|Mercadoria: ", i, "|Quantidade de vendas da mercadoria: ",qnt_vendas)

print ("Fatura do mês : ",sum(vet))
    
