# funções (def)

"""
Funções é um comando que ajuda na organização e a realiza uma determinda
tarefa dentro de um bloco de código. Ajuda também na reutilizadção do código
podendo chama-lá em qualquer parte do programa.
"""

def clubes(corinthians, palmeiras, Campeonato = "indefinido"):
   
   print(f"Titulos do {Campeonato}\n")

   return (f"Corinthians: {corinthians}\nPalmeiras: {palmeiras}")



    

titulos = clubes("31", "26", "Paulistão")
print(titulos)

titulos = clubes("7", "10", "Brasileirão")
print(titulos)

print()

# pratica 2 

def soma(a, b):
   return a + b

N1 = int(input("digite um número: "))
N2 = int(input("digite um número: "))

resultado = soma(N1, N2)
print(f"O resultado da soma é: {resultado}")