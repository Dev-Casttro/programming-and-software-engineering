#while - Loops 
#while = enquanto

#iniciando a variavel 'numero' com 1 
numero = 1 

#enquanto 1 for menor que 5:
while numero <= 5:
    print(numero)

    numero += 1 # soma mais 1 até o valor ser maior - igual a 5. OBS = numero +=1 é igual á numero + numero = 1.

"""
Nosso programa lê a variavel (numero = 1), depois pula para a segunda linha e recebe as instruções.
Enquanto (while) a variavel (numero = 1) for menor - igual á 5, nesse caso 1 é menor 5 então 
ele pula para terceira linha e imprime o valor (1), depois pula para quarta linha e soma +1 na variavel,
ou seja, nossa variavel está valendo (2) agora.
Depois ele repete esse mesmo processo até valer 5, formando um loop de cima para baixo.
"""
print() # para uma linha em branco 

contador = 5 #nossa variavel recebe 5

while contador >= 1:#enquanto 5 for maior - igual 1, subtrai 1 
    print(contador)

    contador -= 1 #decrementa 1 na variavel, subtraindo 1 de 5 até o fim do loop.

#isso faz que contamos de de tras para frente como: 5, 4, 3, 2, 1.
#Podemos descontar 2 tbm, em vez de contador -= 1, usamos contador -= 2 nesse caso ficaria: 5, 3, 1.

print()

cont = 0

while cont < 10:
    cont += 1
    
    print(f"numero: {cont}")
     

else:
    print("Numeros impressos com sucesso!")


#while com if 

Numero = 1 

while Numero < 100:

    print(Numero)

    if Numero == 5:

        break
    Numero += 1


print()

#while dentro de outro while

linha = 0 #variavel linha recebe 0

while linha < 3: #nosso while principal, enquanto linha for menor que 3 

    coluna = 0 # variavel coluna recebe 0 

    while coluna < 3: #Nosso while secundario, enquanto coluna for menor que 3 

        print(f"linha: {linha} --- coluna: {coluna}")#printa os numeros iniciais na tela, assim dando continuidade no loop.

        coluna += 1 #soma +1 no valor da variavel a cada interação.

    linha += 1 #soma +1 no valor a cada interação.

    """
    Nossa variavel linha recebe 0, (linha = 0).
    
    Na segunda linha do código, colocamos nosso while principal, enquanto 0 for menor que 3 (while linha < 3:),
    pule para proximas instruçoes.

    Ok aqui ja criamos o corpo do nosso comando while e dentro dele iniciamos outro comando while.
    
    dentro do nosso loop criamos uma variavel coluna que recebe 0 (coluna = 0).

    colocamos while, enquanto coluna for menor que 3 ( while coluna < 3:) execute o print com os valores iniciais do loop.

    Nosso programa imprimirá, linha: 0 --- coluna: 0.

    então somamos +1 no valor de coluna.

    ainda no while secundario, ele soma +1, então nossa variavel coluna passa a valer 1 e depois ele retorna
    para o while secundario e pergunta 1 é menor que 3 ? sim então ele continua.

    ele pula para o print e imprime: linha: 0 --- coluna: 1.

    depois dessas 3 interações com while secundario, ele pula para o while principal e soma +1.

    então nossa linha passa a valer 1.

    depois ele inicia novamente o while secundario e repete o processo até chegar no print.

    Agora nosso programa irá imprimir o seguinte: linha 1 --- coluna: 0.

    depois ele repete o mesmo processo até o while principal executar 3 loop.

    Assim sempre repetindo o while secundadrio 3 vezes a cada interação do while principal.

    nesse caso ficaria assim pela logica:

    while principal: 1 loop 
        while secundario 3 loop

     while principal: 2 loop 
        while secundario 3 loop

     while principal: 3 loop 
        while secundario 3 loop

    Assim encerra o programa.
    



    """

    

