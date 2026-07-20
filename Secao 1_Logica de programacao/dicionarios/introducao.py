"""
Dicionarios em python

    Introdução ao dicionários
    Diferença entre tuplas, listas e dicionarios 
    por que usar dicionarios ?
"""

#1. Dicionários 
"""
Uma das estruturas de dados embutidas em python que permite armazenar uma coleção de intens.
são indexados por chaves que pode ser qualquer tipo imutavel. Como strings ou números.

Exemplo prático 

suponha que vc queira armazenar informaçãoes de um livro, como o titulo, o autor e o ano da publicação:
"""

livro = {
    "Autor": "George Orwell",
    "Ano" : "1949",
    "Titulo": "1984"
}

print(livro["Ano"])
print()

#2.  Diferença entre tuplas, listas e dicionarios 

frutas = ["Banana", "Uva", "Laranja"] #listas: mutaveis 
print(frutas[1]) #imprimr o intem da lista na posição "1"(indexação começa com 0).

coordenadas = (4.5, 3.6) #tuplas: imutaveis 
print(coordenadas[0])

