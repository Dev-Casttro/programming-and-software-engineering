# revisão das aulas.

# random 

"""
É uma biblioteca ja instalada no python, que permite usar as função random.
"""
import random

print(random.randrange(1, 10)) # gera um número aleatório entre 1 e 10.

print(random.random()) # gera um número  flutuante aleatorio entre 0 e 1.

print(random.randint(10, 20)) # gera um numero inteiro entre dois numeros.

clubes = ["Corinthians", "Palmeiras", "São paulo", "Santos"]
print(random.choice(clubes))  # gera um valor aleatorios da lista.

clubes = ["Corinthians", "Palmeiras", "São paulo", "Santos"]
print(random.shuffle(clubes))  # Embaralha os valores da lista 

# If... else.... elif 

"""
São comandos usados para determinar e processar um código atraves de uma condição. 
"""

user = int(input("digite um numero: "))

if user < 50:
    print("Menor")

else:
    print("Maior")

# Estrutura condicional ternaria 

"""
Estrutura usada somente para condiçoes mais simples. dependendo do seu código recomenda a estrutura classica do IF..else.
"""

senha = int(input("Digite o ID: ")) 
id = "Black_203" if senha == 203 else "errou"
print( f"Bem vindo {id}")


# While 

"""
comando usado para gerar loop, mais usada quando não sabemos o numero de repetições do programa.
"""

cont = 1

while cont <= 3:
    print(cont)

    cont += 1

print()

# For 

""" 
Temos o for mais usado quando sabemos o numero de loops que irá ser executado.

"""

for i in range(1, 5 + 1, 2):
    print(i)