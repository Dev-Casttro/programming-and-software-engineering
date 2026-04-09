# Kwargs, variaves locais vs Globais e nonlocal

# Kwargs

""" Função que exebi dados pessoais"""

def Dados_informacao(**kwargs): # função que recebe dicionario(**Kwargs)

    for chave, valor in kwargs.items(): # pega a chave + valor com kwargs.items()
        print (f"{chave}: {str(valor)}") # imprime a chave + valor.


Dados_informacao(Nome = "gustavo", idade = 22) # chama a função e passa os parâmetros.


# Escopo de variaveis


"""
variaveis locais vs globais 
uso do global 
uso do nonlocal (em funções aninhadas)


Variaveis locais vs globais

uma variavel  definida dentro de uma função é chamada de variavel local,
enquanto uma definida fora de todas as funções é chamada de variavel global.

"""

var_global = "sou uma variavel global"

#definindo a função exemplo

def exem_var():

    global var_global

    # criando uma variavel local dentro da função 
    var_local = "sou var local"

    #imprimindo as variavel local
    print(var_local)

    # imprimindo a variavel global(é possivel acessa-lá, mas
    # para modifica-lá é preciso usar a palavra-chave "global")
    print(var_global)

    var_global = "oi"
    print(var_global)


# chamando a função exemplo que imprimirá as variaveis. 
exem_var()
print(var_global)



