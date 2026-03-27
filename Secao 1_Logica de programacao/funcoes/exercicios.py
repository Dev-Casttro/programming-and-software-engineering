def estatisticas (*args): #função com junção de n argumentos
    
    soma = sum(args) # soma os argumentos 
    return soma / len(args) # len: conta a quantidade de argumentos, calcula a média.

user = input("Digite os numeros para média: ").split() # solicita ao usuario / split(): separa as strings 

lista_num = [int(numero) for numero in user] # cria uma list comprehension para converter as string em numeros.

media = estatisticas(*lista_num) # chama a função e desempacota os valores.
print(media)

""" 
Aqui criamos uma função para receber n argumentos.

*args =  junta os valores de uma função transformando em uma tupla.

soma = sum (args): cria uma variavel chamada soma, utilizamos o sum(args) para a soma dos argumentos e armazenar na variavel soma 

return soma / len(args): depois nois calcula a media para ter o resultado, pegamos a soma e dividimos pela quantidade
de argumentos(len) armazenados na tupla.

até agora ja passamos a função e fizemos o "processamento" dos parâmetros.

Agora vamos definir os parâmetros com usuario.

solicitamos os numeros para somar e calcular a média com split() separando essas strings. 

depois criamos uma lista já convertendo essas strings em inteiro e armazenando dentro dela. Utilizamos o for para "pegar o numero armazenado em user e converter 
de string para inteiro.

depois chamamos a função desempacotando ela para receber os valores separados.

"""