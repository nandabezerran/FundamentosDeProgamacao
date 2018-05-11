#coding: utf-8
n = int(input("Digite a quantidade de contas a serem armazenadas e gerenciadas: "))
MatContas = {}
 
for i in range (1,n+1): #Número de linhas
    print ("Digite o número da conta: ")
    MatContas[(i,1)] = input() #Coluna dos números das contas - 2
    print ("Digite o saldo da conta: ")
    MatContas[(i,2)] = float(input()) #Coluna dos Saldos - 2
#Menu de opções
print("Digite 1 para creditar\n - 2 para debitar\n - 3 para consulta de saldo\n - 4 para transferência\n - 0 para finalizar")
opc = input()
while opc != 0:
    #Opção1 - Creditar
    if opc == 1:
        numeroConta = input("Digite o número da conta: ")
        for i in range (1,n+1):
            #Percorrendo a Matriz
            if numeroConta == MatContas[(i,1)]:
                valor = float(input("Digite o valor a ser creditado: "))
                MatContas[(i,1)] = MatContas[(i,2)] + valor
                print ("Valor creditado com sucesso")
            else:
                print("O número da conta não existe")
    #Opção2 - Debitar 
    if opc == 2:
        numeroConta = input("Digite o número da conta: ")
        for i in range (1,n+1):
            #Percorrendo a Matriz
            if numeroConta == MatContas[(i,1)]:
                valor = float(input("Digite o valor a ser debitado: "))
                MatContas[(i,1)] = MatContas[(i,2)] - valor
                print ("Valor debitado com sucesso")
            else:
                print("O número da conta não existe")
    #Opção3 - Consultar o saldo
    if opc == 3:
        numeroConta = input("Digite o número da conta: ")
        #Percorrendo a Matriz
        if numeroConta == MatContas[(i,1)]:
            print("Saldo da conta ", MatContas[(i,1)],"é: ",MatContas[(i,2)])
        else:
        print("O número da conta não existe")
    #Opção4 - Transferência
    if opc == 4:
            numeroConta = input("Digite o número da conta: ")
        for i in range (1,n+1):
            #Percorrendo a Matriz
            if numeroConta == MatContas[(i,1)]:
                valor = float(input("Digite o valor a ser debitado: "))
                MatContas[(i,1)] = MatContas[(i,2)] - valor
                print ("Valor debitado com sucesso")
            else:
                print("O número da conta não existe")
        numeroConta = input("Digite o número da conta que receberá a transferência: ")
        for i in range (1,n+1):
            #Percorrendo a Matriz
            if numeroConta == MatContas[(i,1)]:
                valor = float(input("Digite o valor a ser creditado: "))
                MatContas[(i,1)] = MatContas[(i,2)] + valor
                print ("Valor transferido com sucesso")
            else:
                print("O número da conta não existe")
for i in range (1,n+1):
    print("Número da conta: ",MatContas[i,1]," Saldo da conta: ",MatContas