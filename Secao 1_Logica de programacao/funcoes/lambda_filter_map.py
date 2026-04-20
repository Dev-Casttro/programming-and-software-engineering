# Função lambda com filter 

"""
Filtramos uma lista para obter apenas números pares 
usando função filter() junto com a função lambda 
"""

# lista 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

print()

# lista com filtração de nomes 

nomes = ["gustavo", "Anna", "joelinton", "Allan"]

nomes_com_A = list(filter(lambda nome: nome[0] == "A", nomes))
print(nomes_com_A)

print()

# filtrando apenas 1 nome da lista

nome_allan = list(filter(lambda nome: nome == "Allan", nomes))
print(nome_allan)


# função lambda com map
"""
Vamos ao exemplo que utilizaremos a função lambda com map() para 
transformar uma lista de números, elevando cada um ao quadrado
"""
""" map() = usado para aplicar uma função especifica em cada elemento da nossa lista"""

num = [1, 2, 3, 4, 5] # lista de numeros 

num_quadrado = list(map(lambda x: x**2, num)) # cria uma lista, onde filtra os elementos elevados ao quadradro.
print(num_quadrado)

print()

# pegando o comprimento de cada palavra de uma lista 

palavras = ["maçã", "pera", "uva", "arroz", "panela"]

palavras_comprimento = list(map(lambda palavra: len(palavra), palavras))
print(palavras_comprimento)

print()

# Exercicios da Aula

# exercicio 1 = retornado numeros impares da listas 

numeros_int = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]

num_impar = list(filter(lambda impar: impar % 2 == 1, numeros_int))
print(num_impar)

print()

numeros_quadrado = list(map(lambda x: x**2, num_impar))
print(numeros_quadrado)



print()

times = corinthians = 30, Palmeiras = 27, São_paulo = 23, Santos = 22

print(times)

