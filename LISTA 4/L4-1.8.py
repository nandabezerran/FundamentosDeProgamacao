#coding; utf-8
#Autor: Fernanda Bezerra
vet[]
for i in range (0,5):
    valor = float(input("Digite o valor da mercadoria: "))
    qnt_vendas = input("Digite a quntidade de vendas: ")
    fatura = valor*qnt_vendas
    vet.append(fatura)
print (sum(vet))
    
