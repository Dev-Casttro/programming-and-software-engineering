# Exercicio for com numeros

#Tabela de multiplicação 

"""
Escreva um programa que peça ao usuario um numero inteiro positivo,
exiba a tabela de multiplicação para esse numero, de 1 a 10.
"""

numero = int(input("Digite um número de sua escolha para tabuada: "))

for i in range(1, 11):
    multi = numero * i 

    

    print(f"{numero} x {i} = {multi}")

print("Fim da tabela de multiplicação")

print()


# Soma dos quadrados 

"""
Escreva um programa e peça ao usuario um numero inteiro positivo N e 
calcule a soma dos quadrados de todos os numeros inteiros de 1 até N 
"""

Numero = int(input("Digite um número de sua escolha para raiz quadrada: ")) # solicita um numero para o usuario.
soma = 0 # variavel para soma dos quadrados 

for i in range(1, Numero + 1 ): # gera um loop de 1 até N (Escolha do ususario).
    
    resultado = i ** 2 # numero de cada posição elevado ao quadrado.

    print(f" quadrado de {i}: {resultado}") # exibi cada posição e o resultado dos  quadrados.

    soma += resultado # soma os quadrados 
    
print(f"Fim da tabela! A soma dos resultados é {soma}") # exibi o total da soma dos quadrados.