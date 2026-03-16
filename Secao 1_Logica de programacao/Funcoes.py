# Funções - Simples 


"""
Em programação, a função é um bloco de código que realiza uma tarefa e pode ser 
executado varias vezes em diferentes partes do programa. As funções ajudam a 
organizar e modularizar o código, tornando-o mais legivel, reutilizavel e facil de manter.
"""

# Criando uma função de soma

def soma(a, b):
    return a + b

resultado = soma (2, 5)
print(resultado)  # Saída: 7

# Podemos reutilizar essa função 

resultado = soma (3, 5)
print(resultado) 

resultado = soma (4, 5)
print(resultado) 

print()

def soma(a, b):
    return a + b

n1 = int(input("Digite o 1 número: "))
n2 = int(input("Digite o 2 número: "))

buy = soma(n1, n2)
print(f"A soma é {buy}")

print()

def saudacao(nome):
    print(f"Óla {nome}!, Bem - vindo")

nome_user = input("Digite seu nome: ")

saudacao(nome_user)