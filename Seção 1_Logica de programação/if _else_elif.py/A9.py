#Estrutura condicional ternaria 

#age = idade 

age = 18 
status = "adulto" if age >= 18 else "menor de idade"
print(status)#saída adulto 

"""
O programa lê nossa variavel (age = 18) depois pula para a segunda linha e 
lê a variavel(status = "adulto") e amarzena esses dados na memoria.
Depois na mesma linha da variaviavel (status = "adulto") nosso programa reconhece que,
foi estabelecido uma condição (if), se age for maior - igual á 18, e dér verdadeiro, ele pula e excuta o codigo
com print(status), caso contrario (falso), ele pula para else e imprime "menor de idade" e encerra o código.
"""

#exercicio de par ou impar usando a cond_ternaria, assim deixando o codigo mais compacto 

n1 = int(input("Digite um número: "))
verif_num = "Par" if n1 % 2 == 0 else "impar"
print(f"{n1} é {verif_num}")

#exercicio verificando score 
Score = int(input("Coloque aqui seu Score: "))
category = "Baixa" if Score < 50 else "Média" if Score < 80 else "Alta"
print(category)