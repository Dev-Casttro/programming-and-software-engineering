"""
Métodos de listas 

    sort(): ordena a lista in-place
    reverse(): inverte a ordem dos elementos in-place 
    count(): conta os números de ocorrençias de um elemento 
    index(): retorna o indice da primeira ocorrençia de um elemento 
"""

# SORT()

numeros = [43, 12, 6, 1, 50]
frutas = ["Banana", "Maça", "Banana", "cereja", "Maça", "Damasco"]

numeros.sort()
print(numeros) #Ordena os elementos em ordem númerica 

print()

frutas.sort()
print(frutas) #Ordena os elementos string em ordem alfabética (A - Z)

# REVERSE

numeros.sort(reverse=True)  
print(numeros) # ordena do maior para o menor 

print()

#OBS: se utilizarmos o false em reverse e ordena na ordem númerica crescente 

# COUNT

ocorrencias_banana = frutas.count("Banana") # conta quantos elementos "x" tem na lista 
print(ocorrencias_banana)

ocorrencias_6 = numeros.count(6) # conta quantos elementos "x" tem na lista númerica 
print(ocorrencias_6)

print()

# INDEX 

indice_banana = frutas.index("Banana") # retorna o indice do nosso elemento "x" na lista 
print(indice_banana) 

print()

# EXERCICIOS 

listas = [23, 11, 89, 34, 11, 56, 78, 90, 23, 45]

# Ordenando a lista 

listas.sort()
print(listas)

# revertendo a ordem da  lista 
listas.sort(reverse=True)
print(listas)

# descobrindo o numero de vezes que o elemento 11 aparece na lista
ocorrencia_11 = listas.count(11)
print(ocorrencia_11)

# descobrindo o indice do elemento 78 da lista 
indice_78 = listas.index(78)
print(indice_78)

# fazendo um tratamento de erro 

try:
    indce_nao_existente =  listas.index(100)
    print(indce_nao_existente)

except ValueError:

    print("O número 100 não está na lista!")

    
