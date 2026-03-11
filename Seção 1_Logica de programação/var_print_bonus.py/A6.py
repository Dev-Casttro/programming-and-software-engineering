#Trabalhando com string parte 2 

#Utilizando o formated string

nome = "alice"
idade = 25
altura = 1.60

#Criando uma mensagem com f-String
mensagem = f"Meu nome é {nome}. Tenho {idade} anos e {altura:.2f} de altura"
print(mensagem)

"""
f-String: é uma forma de formatar strings em python 3.6 ou superior, onde 
voçê pode incorporar expressões entre chaves {} que serão avaliadas em tempo de execução.
"""

#Upper() converte para maiúsculo 
texto = "Óla mundo"
Texto_upper = texto.upper()
print(Texto_upper)

#Lower() converte para minúsculo
texto = "Óla mundo"
Texto_lower = texto.lower()
print(Texto_lower)

#Capitalize converte a primeira letra em maiúsculo
texto_capitalize = texto.capitalize ()
print(texto_capitalize)

#cont = Conta quantas letras maiúsculas ou minúsculas contém no texto.
ocorrencia = texto.count("o")
print(ocorrencia)

#replace = subistitui uma string por outra 
texto_substituido = texto.replace("mundo", "amigo")
print(texto_substituido)

#Exercicios 

nome = "Maria"
sobrenome = "Silva"
idade = 30

nome_complteto = f"{nome} {sobrenome}"
print(nome_complteto)

mensagem = f"Meu nome é {nome_complteto}. Tenho {idade} anos"

print(mensagem)

#Exerciocio2

Frase = "Python é uma linguagem de programaçao poderosa" 
quantidade = len(Frase)
print(quantidade)

palavra = Frase.split()[0]
print("primeira palavra da frase:", palavra)

Frase_maiuscula = Frase.upper()
print(Frase_maiuscula)

frase_substitui = Frase.replace("poderosa", "incrivel")
print(frase_substitui)