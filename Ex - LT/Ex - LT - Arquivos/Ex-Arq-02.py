#coding: utf-8
#Autor: Fernanda Bezerra
Alunos = []
Arquivo = open('Aluno.txt', 'r')
texto = Arquivo.read()
Arquivo = open('Aluno.txt', 'w')
Nome = input("Digite o nome do aluno: ")
Alunos.append(Nome)
Número = int(input("Digite o numero do aluno: "))
Alunos.append(Número)
Curso = input("Digite o curso do aluno: ")
Alunos.append(Curso)
Nota1 = float(input("Digite a primeira nota do aluno: "))
Alunos.append(Nota1)
Nota2 = float(input("Digite a segunda nota do aluno: "))
Alunos.append(Nota2)
Arquivo.write(texto)
Arquivo.write('Nome:%s\n' % (Alunos[0]))
Arquivo.write('Número:%s\n' % (Alunos[1]))
Arquivo.write('Curso:%s\n' % (Alunos[2]))
Arquivo.write('Nota 1:%s\n' % (Alunos[3]))
Arquivo.write('Nota 2:%s\n' % (Alunos[4]))
Arquivo.close()

