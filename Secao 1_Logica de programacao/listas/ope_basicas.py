# Operações basicas com listas 

""" Adicionar elementos: append() e insert()
    remover elementos: remove() e pop()
    concatenar listas: + e extend()
    repetir listas: *
    verificar se um imtem está na lista: in """

# Adicionar elementos

#append() - adiciona um intem no final da lista 
frutas = ["Banana", "Maçã"]
frutas.append("Maracuja")
print(frutas)

print()

#insert() - insere um intem em uma posição especifica 
frutas = ["Banana", "Maçã"]
frutas.insert(1, "Abacate") #inserindo parâmetro na segunda posição da lista. 
print(frutas)

print()

#remover elementos

#remove() - remove o primeiro intem da lista que tem o valor especificado
frutas = ["Banana", "Maçã"]
frutas.remove("Banana")
print(frutas)

#pop() - remove o parãmetro atraves do indice 
frutas = ["Banana", "Maçã", "Abacate"]
frutas.pop(1)
frutas.pop()
print(frutas)

print()

# concatenar listas

# + - uni duas listas 

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1 + lista2)

 #extend()
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista1.extend(lista2)
print(lista1)

print()

# repetir listas

# * - repete os parâmetros dentro da lista em um determinado número de vezes.
repeticao = ["a", "b"] * 2
print(repeticao) 

print()

# verificar se um imtem está na lista

#in

# vai verificar se tem o elemento "banana" na lista e retorna um valor booleano (false or true)
frutas = ["Banana", "Maçã", "Abacate"]
print("Banana" in frutas)
print("Uva" in frutas)
