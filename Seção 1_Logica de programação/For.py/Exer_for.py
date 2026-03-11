"""
Escreva um programa que utilize o loop for para multiplicar os 
números de 1 a 5 e imprima o resultado de cada etapa e o resultado final.
"""

multi = 1 # variavel multi que recebe 1 

for i in range(1, 6): # usando o for com range para gerar um loop.
    multi *= i  # multiplica o valor da variavel multi com valor de i.

    print(f"multiplicando por {i}, o resultado parcial é {multi}") # print com f-string para imprimir caracteres e valores 

print(f" O resultado final da multiplicação é {multi}") #resultado final da multiplicação armazenada na variavel multi.

print()

"""
Escreva um programa que peça ao usuario um número inteiro N e some todos os 
números pares de 1 até N, incluindo o proprio N (se for PAR).
"""

soma = 0 # variavel soma que recebe 0 
numero = int(input("Digite um número: ")) # solicita um numero para o usuario.

for n  in range(2, numero + 1, 2): # usamos for com range iniciando com 2 até o valor de numero, com passos de 2 
  
    soma += n # soma os numeros pares gerados no loop.

print(f"A soma dos números pares de 1 até {numero} é {soma}") # mostra os resultados da soma. 



