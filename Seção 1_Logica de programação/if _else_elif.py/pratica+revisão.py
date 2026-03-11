#Exercicio com if...else..elif

"""
IF, ELSE, ELIF: Significa (SE, SENÃO e SENÃO-SE) em portugues, é uma estrutura de decisão onde
o programa pode tomar decisões igual na vida real.


exemplo: 

SE estiver chovendo - eu levo guarda -chuva
SENÃO - eu não levo 

o código só executa se a condição for verdadeira (true)

SENÃO - SE: serve para mais de uma condição no código.

SE a nota for de 0-4 == Baixa 
SENÑAO - SE a nota for de 5-8 == média 
ELSE - a nota de 9-10 == alta 

"""

nota = float(input("Digite sua nota: (0-10)"))
nota2 = float(input("Digite sua nota: (0-10) "))

media = (nota + nota2)/2

if media >= 7:
    print("Aprovado")

else: 
    print("Reprovado")

#Exercicios com listas 

frutas = ["maçã", "Uva", "morango", "Banana", "pera"]

print(frutas)

select = frutas[0]
print(select)

select2 = frutas[-1]
print(select2)

# O que é uma lista ?

"""
Uma lista é uma estrutura de dados.
Uma forma organizada de guardar vários valores dentro de uma única variável.
Em vez de guardar 1 valor, a lista guarda N valores 

pense um uma mochila.
A mochila é a lista 
Cada objeto dentro é um item da lista 
Cada intem tem uma posição

voçê pode: 

colocar coisa 
tirar coisas
trocar coisas de lugar

Uma lista guarda vários dados relacionados 

lista de notas
lista de nomes
lista de produtos

lista é ordenada 
os elementos tem ordem deifinida 

cada item tem um indice (posição), começando com 0

lista é mutavel, podendo: adicionar, remover e modificar intens.
"""
#Exercicio da aula de ontem 
#estrutura condicional ternaria 

n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua nota: "))

media = "Aprovado" if (n1+n2)/2 >= 7 else "reprovado"
print(media)
