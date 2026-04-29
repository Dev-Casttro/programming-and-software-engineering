# Introdução as listas 

""" 
Listas são uma das estrutura de dados mais fundamentais em python. Elas são 
coleções ordenadas de intens (que podem ser qualquer tipo) e são muito versateis.

vamos supor que voçê quer armazenar as notas de um aluno em diferentes matérias. Uma 
lista é perfeita pra isso.
"""

# definindo uma lista de notas de um aluno
notas_aluno = [5, 10, 8, 9]
print(notas_aluno)

#Exemplo 2 
""" listas vs Tuplas: Ambas podem armazenar multiplos intens, mas as listas são mutaveis 
(voçê pode alterar seu conteúdo) enquanto as tuplas são imutaveis."""

lista = [1, 2, 3]
lista[0] = 100
lista[1] = 50 # isso é válido
print(lista)

tupla = (1, 2, 3) # gera um erro. imutaveis!

print("_____________________________")

"""
Criando e acessando listas

    Como criar uma lista: minha_lista = [parâmetros]
    Acessando elementos pelo índice
    índices negativos para acessar elementos mo final da lista.
"""

#lista com parâmetros do tipo "int"
numeros = [10, 20, 30, 40]
print(numeros)

#lista com parâmetro do tipo "string"
lista_strings = ["frutas", "Legumes", "Vegetais"]
print(lista_strings)

#lista com parâmetros de diversos tipos.
lista_types = [10, "azul", 7.5, ["a", "b"], True]
print(lista_types)

# Acessando as listas armazenadas em uma tupla.
acessando_listas = (lista_types, lista_strings, numeros)
print(acessando_listas[0], lista_strings[0]) #Acessando a lista e seus elementos pelo ìndice.

# Acessando o ultimo elemento 
acessando_listas = (lista_types, lista_strings, numeros)
print(acessando_listas[-1], lista_strings[-1])

