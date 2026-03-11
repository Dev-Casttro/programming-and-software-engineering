#Exerc com listas

listas = ["A", "B", "C", "D", "E"] # variavel listas com letras do alfabeto 

for item in listas: # loop com variavel item substituindo cada posição da lista.
    print(item) # imprime os elementos de nossa lista 

    if item == "C": # se chegar no elemento "C" irá imprimir: A B C 
        break #encerra o programa 


print()

frutas = ["Banana", "Maçã", "Pera"]

for Frutas in frutas:
    print(Frutas)


print()



User = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for user in User:

    if user % 2 == 0:
        print(f"{user} - Par")

    else:

        print(f"{user} - Impar")


print()

# Exercicio de lista de compra

intem_compras = ["Leite", "banana", "bife", "Arroz"]

for intem in intem_compras:

    print(f"Eu preciso comprar: {intem}")

print()

#Exercicio estrelas 

for i in range (5, 0, -1):

    print("*" * i)

# Exercicio lista de palavras, verifica as palavras com mais de quatro letras da lista.

palavras = ["carro", "casa", "quarto", "cozinha"]

for palavras in palavras:

    if len(palavras) > 4:
        
        print(palavras)

    
    



