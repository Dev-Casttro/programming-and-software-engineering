#random 

#Numeros randomicos - numeros aleatorios 

import random   
print(random.randrange(1,10)) #randrange é de um numero até tal numero 

print (random.random())#random gera um numero flutuante aleatorio entre 0 e 1

print(random.randint(10,20))#gera um numero inteiro entre dois numeros, exemplo, entre 10 e 20 gera 15.

#Escolher aleatoriamente um intem da lista 
frutas = ["maçã", "banana", "maracuja"] 
print(random.choice(frutas)) # escolhe uma fruta da lista 

#Embaralhar aleatoriamente uma lista 
numeros = [1, 2, 3, 4, 5]
(random.shuffle(numeros))
print(numeros)#A lista "numeros" agora está embaralhada

print (random.uniform(5.5, 10.6))
