#coding: utf-8
#Autor: Fernanda Bezerra
voo = []
origem = []
destino = []
lugares = []
for i in range (0,3):
	voo = input("Número do vôo: ")
	origem = input("Origem do vôo: ")
	destino = input("Destino do vôo: ")
	lugares = input("Quantidade de lugares no vôo: ")
	op = 0
while op != 3:
	print("1- CONSULTAR 2- RESERVAR 3- FINALIZAR")
	op = int(input())
	if op == 1:
		op_2= int(input("1- CONSULTA POR VOO 2- CONSULTA POR ORIGEM 3- CONSULTA POR DESTINO"))
		if op_2 == 1:
			num_voo = int(input("Qual o número do vôo?: "))
			if num_voo <= 3:
				print ("Voo: ",voo[num_voo],"Origem: ",origem[num_voo],"Destino: ",destino[num_voo],"Cadeiras disponíveis: ",lugares[num_voo])
			else:
				print("Vôo inexistente")
		if op_2 == 2:
			origem_1 = raw_input("Qual a origem do vôo?: ")
			aux = origem[origem_1]
			if aux <= 3:
				print ("Voo: ",voo[aux],"Origem: ",origem[aux],"Destino: ",destino[aux],"Cadeiras disponíveis: ",lugares[aux])
			else:
				print("Origem inexistente")
		if op_2 == 3:
			destino_1 = raw_input("Qual o destino do vôo?: ")
			aux1 = destinp.index(destino_1)
			if aux1 <= 3:
				print ("Voo: ",voo[aux1],"Origem: ",origem[aux1],"Destino: ",destino[aux1],"Cadeiras disponíveis: ",lugares[aux1])
			else:
				print("Destino inexistente")
	if op == 2:
		num_voo = int(input("Qual o número do vôo?: "))
		if num_voo <= 3:
			if lugares[num_voo] != 0:
				print("Reserva concluída")
			elif lugares[num_voo] == 0:
				print("Vôo sem lugares disponíveis")
			else:
				print("Vôo inexistente")

