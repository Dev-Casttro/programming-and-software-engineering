# Exercicios Fabrica de operações matematicas

def Fabrica_operacoes(str):

    def soma(a, b):
        
        return a + b
    
    def subtracao(a, b):
        
        return a - b
    
    def multiplicacao(a, b):
        
        return a * b
    
    def divisao(a, b):
        
        return a / b
    
    if str == "soma":

        return soma
    
    elif str == "subtracao":

        return subtracao
    
    elif str == "multiplicacao":

        return multiplicacao
    
    elif str == "divisao":

        return divisao
    
    
adicao = Fabrica_operacoes("soma")
print(adicao(2, 2)) # Saída = 4

subtracao= Fabrica_operacoes("subtracao")
print(subtracao(10, 2))  # Saída = 8

multiplicacao = Fabrica_operacoes("multiplicacao")
print(multiplicacao(2, 2))  # Saída = 4

divisao = Fabrica_operacoes("divisao")
print(divisao(10, 2))  # Saída = 5

print()


# Correção do professor # Exercicios Fabrica de operações matematicas

    
def Fabrica_operacoes(operacao):

    def soma(*args):
        
        return sum(args)
    
    def subtracao(*args):
        
        resultado = args[0] # pega o primeiro número da lista [0]

        for num in args[1:]: # pega o segundo número da lista em diante [1:]

            resultado = resultado - num

            return resultado
    
    def multiplicacao(*args): # função que percorre a lista de argumentos e multiplica.
        
        resultado = 1  # vai armazenar o resultado da multiplição a cada interação e multiplicar pelo proximo args.

        for num in args:

            resultado *= num
            return resultado 
    
    def divisao(*args):
        
        resultado = args[0]

        for num in args[1:]:

            if num == 0:
                raise ValueError("Divisão não suportada") # Ele retorna o erro do sistema para o user.
            
            resultado /= num

            return resultado 
    
    if operacao == "soma":

        return soma
    
    elif operacao == "subtracao":

        return subtracao
    
    elif operacao == "multiplicacao":

        return multiplicacao
    
    elif operacao == "divisao":

        return divisao
    
    else:
        def operacao_inexistente(*args):
            return "divisão não suportada"
        
        return operacao_inexistente
    
    
adicao = Fabrica_operacoes("soma")
print(adicao(2, 2)) # Saída = 4

subtracao= Fabrica_operacoes("subtracao")
print(subtracao(10, 2))  # Saída = 8

multiplicacao = Fabrica_operacoes("multiplicacao")
print(multiplicacao(2, 2))  # Saída = 4

divisao = Fabrica_operacoes("divisao")
print(divisao(10, 2))  # Saída = 5


    

