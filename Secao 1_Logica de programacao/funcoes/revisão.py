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


print()

# Pratica 3 

while True:

   def dados_cliente(nome, args_idade, args_data_nascimento):

      print(f"\nDados do cliente:\nNome: {nome}\nIdade: {args_idade}\nNascimento: {args_data_nascimento}")
      
      print(args_idade + args_data_nascimento)

      return nome, *args_idade, *args_data_nascimento

   nome_cliente = input("Nome: ")
   idade_cliente = input("Idade: ")
   data_nasc_cliente = input("Data de nascimento: ")

   dados_cliente(nome_cliente, idade_cliente, data_nasc_cliente)

   print("Cadastro concluido com sucesso!")
