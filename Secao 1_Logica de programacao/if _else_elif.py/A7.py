#if...elif...then...com and... etc.

#Python  função (if), ou seja, (Se ...)
numero1 = 90
numero2 = 12

"""
if (se) a variavel numero1 for maior que a variavel numero2 imprima,
print(f"{numero1} é maior que {numero2}")
"""
if numero1 > numero2: # se for verdadeiro ele imprime, se caso for falso ele trava e não imprime
    print(f"{numero1} é maior que {numero2}") 

#função if...elif 
#elif (Senão -Se...)
N1 = 6
N2 = 6 

if N1 > N2:
    print(f"{N1} é maior que {N2}")

elif N1 == N2:
    print(f"{N1} é igual a {N2}")


#EXERCICIO - Adivinhe o número secreto

#Else = Senão 

#Define o número secreto que o usuario deve adivinhar 

N_secreto = 7 
#Solicita ao usuario que insira um numero de 1 a 10 

Usuario= int(input("Adivinhe o número secreto entre 1 a 10: "))
#verifica se o numero inserido pelo user é igual ao numero secreto 

if Usuario == N_secreto:
    print("ACERTOU!")
#se o usuario adivinhar e for true imprima a mensagem de sucesso.

else:
    print("ERROU!")

#Se o usuario errar e for false, imprima a mensagem de erro.


#Exercicios2 - verificando se é maior de idade 

#define a idade minima para execução 
elei_gov = 18

#Solicita a idade para o eleitor 
eleitor = int(input("Informe sua idade: "))

# se maior de idade imprima (Avançar)
if eleitor >= elei_gov:
    print("Avançar...")

#Se  menor de idade imprima o comunicado.
elif eleitor < elei_gov:
    print(" A votação só pode ser feita por maiores de 18 anos")

#And - E

n1 = 50
n2 = 21
n3 = 200

if n1 > n2 and n3 > n1:
    print("As duas condições são verdadeiras")


#Exercicio - classificaçao de Notas 

Aluno_Nota = int(input(" Digite a nota do aluno(a), entre (0 a 100): "))

if Aluno_Nota >= 90 and Aluno_Nota <= 100:
    print(f"Nota: {Aluno_Nota}")
    print(f"Excelente!")

elif Aluno_Nota>= 70 and Aluno_Nota<= 89:
    print(f"Nota: {Aluno_Nota}")
    print("Bom!")

elif Aluno_Nota>= 50 and Aluno_Nota<= 69:
    print(f"Nota: {Aluno_Nota}")
    print("Satisfatório!")

elif Aluno_Nota <= 49:
    print(f"Nota: {Aluno_Nota}")
    print("Insufuciente!")

#xercicio - Calculadora de descontos 

compra_valor = float(input("Insira o valor da compra: "))

if compra_valor > 1000:

    print("Você recebeu 20% de desconto")

    valor_desconto = compra_valor * 20 / 100
    total_valor = compra_valor - valor_desconto

    print(f"Desconto: {valor_desconto:.2f}")
    print(f"Total: {total_valor:.2f}")

elif compra_valor >= 500 and compra_valor <= 1000:
    print("Você recebeu 10% de desconto ")

    valor_desconto = compra_valor * 10 / 100
    total_valor = compra_valor - valor_desconto

    print(f"Desconto: {valor_desconto:.2f}")
    print(f"Total: {total_valor:.2f}")

else:
    print(f"Compras abaixo de {compra_valor} não recebe desconto!")