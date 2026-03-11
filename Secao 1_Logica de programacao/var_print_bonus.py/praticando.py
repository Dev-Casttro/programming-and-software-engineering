#sistema de calculos de Nota 

nome = str(input("Digite o nome: ")) # Variavel nome do tipo (str), onde solicita o nome do aluno com comando de entrada (input)
Idade = int(input("Digite sua idade: ")) # var idade do tipo (int), solicita a idade do aluno...     
RA = int (input("Digite seu RA: ")) # var RA do tipo int, solicita o numero de registro do aluno        

print("\nNome: ", nome, "\nidade: ", Idade, "\nRA: ", RA)

"""
Aqui Mostramos na tela os dados do Aluno, 
com o comando de saida (print) e (/n) para pular uma linha 
"""

Dados = input (str("\nConfirme seus Dados com Sim ou Não: "))#Aqui pedimos para o aluno confirmar os dados 

print("\nVamos Calcular sua Média do primeiro Semestre")

n1 = float(input("Digite sua nota do P1: "))#Float para variavel do tipo numerico
n2 = float(input("Digite sua nota do P2: "))#input para entrada de dados, onde solicita os pontos 
n3 = float(input("Digite sua nota do P3: "))
n4 = float(input("Digite sua nota do P4: "))
"""
Criamos quatro variaveis do tipo (Float) para o aluno colocar seus pontos do semestre,
e podermos calcular sua media do semestre 
"""

Media = n1 + n2 + n3 + n4 + n4 / 2 #Aqui somamos as notas e dividimos por 2 para saber a media                                                                                                                                                

print("\nNome: ", nome, "\nNota S1: ", n1, "\nNota S2: ", n2, "\nNota S3: ", n1,  "\nNota S4: ", n4, "\nMedia: ", Media)

