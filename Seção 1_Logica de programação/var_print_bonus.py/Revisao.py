# VARIÁVEIS E TIPOS 

print("print executado com sucesso")
# O print é um comando de sáida 

inteiro = 42 
print (inteiro) # Variavel: Interiro do tipo (Int)

#Variavel é um espaço, onde vai ser armazenado um valor (Dados) na memória.

Flutuante = 42.0
print(Flutuante)#Type = Float 

complexo = 3 + 4j
print (complexo) #type = complex

String = "Texto"
print (String) #Tipo = str 

Lista = [] # tipo list, mutavel 

tuplas = () #tipo = tuple, imutavel 

conjuto = {} #tipo = set, não ordenada - intens unicos 

dicionario = {} #tipo = dict - não ordenada, com pares e chave-valor 
 
booleano = true or False #tipo - boo

#EXERCICIOS 

idade = 25 #tipo - int

nome = "João" #tipo - str 

Saldo = 100.50 #tipo - float 

soma = idade + Saldo
print (soma)

n1 = 7.5
n2 = 8.3
n3 = 6.9

media = n1 + n2 + n3 / 2

print(format(media,".2f"))

#INPUT 

nome = input("Digite o nome: ") #Input é um comando de entrada. 
Nota1 = float(input("digite sua nota "))#Usamos o float para converte uma string em um valor.
"""
Se tirarmos o float ele vai armazenar o valor na variavel como string, nesse caso, estamos trabalhando com notas,
então devemos converter para o tipo numerico Float ou int.
"""

#RANDOM 

import random 
print(random.randrange(1,10))#randrange gera numeros aleatorios de 1 a 10 
print(random.random())#random qualquer coisa com numero quebrado 

frutas = ["maça", "banana", "uva"]
print(random.choice(frutas))#Choice escolhe um inten aleatorio da lista 

frutas = ["maça", "banana", "uva"]
print(random.shuffle(frutas))#Shuffle embaralha a lista 

#Amigo secreto 

Familia = ["amabilly ","Gustavo ","karina","Kaua","Maura","Juilia"]

print ("/nBEM VINDO AO AMIGO SECRETO DA FAMILIA ")
print("Vamos revelar a pessoa que vc tirou")

Soma = input("Após a pergunta revelo a pessoa \n Quantos é 1 + 1: ")
Print("\nAcertou...\n Não Mostre a pessoa seu burro(a)")

import random

print(random.choice(familia))


 