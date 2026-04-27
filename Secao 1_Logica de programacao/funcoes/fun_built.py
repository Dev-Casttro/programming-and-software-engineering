# funções internas 

"""
são funções que já vem embutidas na linguagem pytho, são disponiveis sem 
a necessidade de importar.

- print(), len(), input(), etc.
- conversão de tipos: int(), float(), str(), etc>
"""

# funções internas 

# print() = utilizado para imprimir valores na tela

nome = "Gustavo"
print("Olá", nome) 

# len = utilizado para ler o comprimento da lista

lista = [1, 2, 3]

print(len(lista))

# input = utilizado para entrada de dados 

"""dado = input("Nome: ")
print(dado)"""

print()


# conversão de tipos

#int

num_decimal = "7.9"
num_int = int(float(num_decimal))

print(num_decimal)

""" primeiramente convertemos a string para float, porque não podemos convertela
para inteiro diretamente. """

#float

num_str = "5.6"
num_float = float(num_str)
print(num_float)

# str

# converte um valor para texto

numero = 123

numero_str = str(numero)
print(numero_str)


""" Existem muitas outras funções built -in no python,
essas foram somente as principais."""

print()

# RECURSÃO 

"""
- Funções que chamam a si mesmas 
- problemas classicos, como o calculo de fatorial
- riscos e ilimitações da recursão em python
"""

def conta_regressiva(n):

    if n > 0:
        
        print(n)
        
        conta_regressiva(n - 1)
    
conta_regressiva(5)

print()

# problemas classicos, como o calculo de fatorial

def fatorial(n):

    if n == 0:
        return 1 
    
    else:
        return n * fatorial(n - 1)
    
print(fatorial(5))
print()

# documentação 

def soma (a,b):

    """Calcula a soma de dois parâmetro da função """

    return a + b

print (soma(2, 2))
print(soma.__doc__) #retorna a documentação dentro da função 

print()

# Anotações do tipo type hints

def multiplicar(a: int, b: int) -> int:

    return a * b

print(multiplicar(2, 2))

"""
No exemplo acima a: int e b: int, indicam que os parâmetros devem ser inteiros 
e a anotação -> indica que a função deve retornar um valor inteiro.
"""