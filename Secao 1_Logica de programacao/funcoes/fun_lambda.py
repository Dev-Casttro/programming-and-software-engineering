# Funções Anônimas (Lambda) 

"""
- definições e uso 
- Limitações em relação as regulares 

Funções lambda são funções anônimas de pequena extensão. Ao contrario de uma 
função definida com def, a lambda pode ter apenas uma expressão e retorna implicitamente 
o resultado dessa expressão. Ela é frequentemente usada para pequenas operações que são convenientes 
de se definir sem nomear uma função completa.

"""

# exemplo 1 - definição e uso 
# função regular para dobrar um número

def dobrar(n):
    return n * 2

print(dobrar(5)) # Saída = 10 

# funcão lambda para dobrar um número 

dobrar_lambda = lambda n: n * 2 

print(dobrar_lambda(5)) # Saída = 10 


# - Limitações em relação as regulares 

def Classificar_num(n):

    if n < 0:

        return "Negativo"
    
    elif n == 0:

        return "Zero"
    
    else:

        return "Positivo"

print(Classificar_num(-4))

# funções lambda com sorted 

""" Suponha que vc tenha uma lista de tuplas representando 
pessoas e suas idades, e vc queira classifica-las por idade."""

pessoas = [("gustavo", 22), ("amabilly", 20), ("Jeff", 42)]
pessoas_ordenadas = sorted (pessoas, key=lambda x: x[1])

print(pessoas_ordenadas)

"""
Sorted() é uma função built-in que retorna uma nova lista contendo todos os intens 
em ordem crescente.
"""