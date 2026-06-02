"""
Listas aninhada (listas de listas)  

    Acessando listas dentro de listas
    Utilizando loops aninhados para interar sobre elas.

    - listas aninhdas são basicamente listas que tem outras listas 
    como seus elementos. Elas são uteis em muitas situações, especialmente ao representar estruturas
    bidimensionais como matrizes.
"""

# 1. Criando listas aninhadas 

# Vamos considerar que queremos representar uma matriz 3x3

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Aqui a matriz é uma lista de 3 elemntos, onde cada elemento é uma lista de 3 elementos.

# Acessando listas aninhadas 

""" para acessar um elemento especifico voçê precisa especificar dois indices: o indice da lista externa
e o indice da lista interna.

exemplo: acessando o número 5 
"""

elemento = matriz[1][2]
print(elemento)

# 3 utilizando loops aninhados para interar 

# para interar sobre cada elemento da matriz, utilizamos o loop For aninhados 

#loop externo: intera sobre cada linha da matriz 
for linha in matriz:

    for numero in linha:

        print(numero, end=' ')
    
    print()

# Exercicios 

#vamos considerar que queremos construir uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor= matriz[1][2]
print(valor)

print()

#Exercicio 2 
soma = 0 

for linha in matriz:

    for numero in linha:

        soma += numero

print(soma)
