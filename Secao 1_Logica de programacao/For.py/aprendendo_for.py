#For é um laço de repetição
# Função range para imprimir os numeros inteiros.

for j in range(1, 11):
    print(j)


"""
Explicação do loop: o loop sera executado para cada valor de i na seguençia gerada,
por range(1, 11) o que significa que ele sera executado 10 vezes, com i assumindo os valores
de 1 a 10, um de cada vez.

"""

# Diferença entre WHILE e fOR.

"""
While: geralmente usado para criar um loop, quando não sabemos o número de repetição,
usamos sempre com base a uma condição verdadeira para gerar o loop.

For: geralmente usado quando sabemos o numero de repetiçao, usado mais para 
controle de sequencia de elementos (listas, tuplas, dicionarios)
"""
print()


# for = utilizando numeros

for i in range(10, 0, -1): # aqui ele vai ler de 10 - 0, decrementando 1, gerando uma contagem de trás para frente.
    print(i)                # Saida será: 10, 9, 8...1

print()

# for de 1 até 10 pulando de 2 em 2.

for i in range(1, 10, 2): 
    print(i)           

# Soam dos numeros impares

soma = 0 #Inicializando a variavel para aarmazenar a soma 

for i in range(1, 10, 2): # interando de 1 a 10 pulando de 2 em 2, capturando os numeros impares 
    print(f"Número impar atual: {i}")

    soma += i # Adicionando o numero impar autual a soma 

    print(f"\n A soma dos numeros impar atual é {soma}")