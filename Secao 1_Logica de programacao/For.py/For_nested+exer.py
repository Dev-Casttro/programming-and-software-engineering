# For nested 

"""
Refere - se ao um loop (for) dentro do outro loop (for).
"""

# Exemplos de loops aninhados

for i in range (1, 4):

    for j in range (1, 4):

        print(f"{i} * {j} = {i * j}")

"""
Para cada interação de (i) o (j) executa 3 vezes. 

exemplo:

i = 1
    j = 1, 2 ,3 

i = 2 
    j = 1, 2, 3

etc.
"""

print()

# Compreensão de lista 

quadrados_impar = [x**2 for x in range (1,11) if x % 2 != 0]
print(quadrados_impar)

"""
está explicação vai ta na ordem que o programa vai ler a lista.


for x in range (1,11): Essa parte o programa ira substituir o valor de (x) de 1 a 10.

if x % 2 != 0 : verifica se o resto da divisão de x por 2 vai ser diferente de 0.

x**2 : Caso (if x % 2 != 0) seja true, eleva x ao quadrado. 

print(quadrados_impar) : Executa o valor da lista definido de acordo com o processamneto da lista. 


"""

print()

# compreensão de lista 2 

quadrados_impa = []

for x in range (1, 11):

    if x % 2 != 0:

        quadrados_impa.append(x**2)

print(f"{quadrados_impa}")

print()

#Exercicios com caracteres cosoantes 
texto = "Hello World"

consoantes = [char for char in texto if char.lower() not in "aeiou"]
print(consoantes)

print()

# consoantes = [char for char in texto if char.lower() not in "aeiou"]

exemplo_2 = []      # lista vazia para receber os caracteres

for letra in texto: # loop para verificar cada letra na variavel texto

    if letra.lower() not in "aeiou": # transforma os char em minusculo e verifica se é vogal

        exemplo_2.append(letra) #adiciona as consoantes na lista vazia 

print(exemplo_2) # mostra o resultado na tela.

print()

# EXERCICIO 

"""
Crie um programa em python que solicite um numero inteiro positivo e calcule o fatorial do msm.
"""

fatorial = int(input("Digite um numero inteiro positivo: "))

multi = 1

for i in range(1, fatorial + 1):
    
    multi = multi * i 

print (f" O fatorial de {fatorial} é {multi}")

  