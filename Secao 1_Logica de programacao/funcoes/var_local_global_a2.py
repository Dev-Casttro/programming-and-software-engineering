# uso do global

"""
Para modificar uma variavel global dentro de uma fução,
devemos usar a palavra-chave "global"
"""
# definindo uma variavel chamada contador e inicializando com 0 
contador = 0

# definindo uma função incrementar contador
def incrementar_contador():
    
    # informando a função que vamos usar a variavel global e não local.
    global contador 

    # incrementando o valor da variavel global

    contador += 1 

    # imprime o contador 
    print (contador)

# chamando a função incrementar contador pela primeira vez
# isso incrementa o contador para 1 e imprime o valor.
incrementar_contador()

incrementar_contador()

incrementar_contador()

print()

# uso do nonlocal (funções aninhadas)

"""
A palavra chave nonlocal é usada para trabalhar com variaveis em um escopo mais 
proximo, mas não global, como em funções aninhadas 
"""

# criando uma função externa
def funcao_externa():

    # variavel externa recebe uma string auto se indentificando
    variavel_externa = "eu sou externa"

    # imprime a variavel externa na tela
    print(variavel_externa)

    # função aninhada como função_interna 
    def funcao_interna():

        # nonlocal recebe a variavel_externa, para modifica-lá (nonlocal)
        nonlocal variavel_externa

        # aqui modificamos a variavel e imprimimos na tela
        variavel_externa = "Eu fui modificada pela função interna"
        print(variavel_externa)

    # chama a função interna 
    funcao_interna()

    # imprime a variavel modificada
    print(variavel_externa)

# chama a função externa
funcao_externa()






