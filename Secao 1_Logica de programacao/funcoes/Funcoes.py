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

print()



"""
Em Python, ao definir uma função, voçê pode atribuir valores padrão aos parâmetros da função.
Esses valores padrão são chamados de "Argumentos default" (Padrão) e permitem que voçê chame a 
função sem precisar fornecer valores para esses parâmetros, pois eles ja têm um valor pré - deifinido.

Por outro lado, os "Argumentos non-default" (Não padrão) são aqueles que não, possuem um valor padrão atribuido
na definição da função e, portanto, precisam ser fornecidos como argumentos quando a função é chamada.

"""



# Argumentos Default e non-default


def exibir_informacoes(nome, idade, cidade = "Desconhecida"):

    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")


# Argumentos sem valores default
exibir_informacoes("Gustavo", 22, "São Paulo\n")

exibir_informacoes("Amabilly", 22)

print()

# varios argumentos com *args 

""" 
Parâmetro especial *args que permite receber um nùmero variavel de argumentos numericos.
Dentro da função, os argumentos são tratados como uma tupla.
"""

def soma(*args):

    """ Função que retorna a soma de vários números"""


    resultado = sum(args) # sum = soma os números 
    return resultado  # retorna o resultado da soma 

total = soma(1, 2, 3, 4) # total recebe a função com parâmetros.
print(total) # exibi o resultado na tela 

"""
Dessa forma, a função soma() é capaz de lidar com qualquer quantidade de argumentos
númericos e retorna soma total desses números.
"""