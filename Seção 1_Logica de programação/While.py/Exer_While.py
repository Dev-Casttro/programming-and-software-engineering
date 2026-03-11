#Exercicios while

"""
Crie um algoritmo que solicite uma senha ao usuario, o loop 
só deverá ser encerrado só quando a senha estiver correta.
"""

senha = "Sccp1910"
cont = 1 


while cont <= 3:

    senha_user = input("Digite a senha: ")

    if senha != senha_user:

        print("Senha incorreta! tente novamente.")
        print(f"{cont}º tentativa.")
    
    else: 
        print("Senha correta!")

        break
    
    
    cont += 1 


#execercicio 2

#cria um loop infinito. Até o user digitar sair. 
while True:

    user_input = input("Digite 'Sair' para encerrar: ")

    if user_input == 'Sair':

        print("Programa encerrado !")

    break


#Adivinhe o número secreto 

import random #importa o modulo random para gerar um numero aleatorio.

N_secret = random.randint(1,10) #usamos random.randint para gerar e amarzenar um numero aleatorio para a var.
tentativas = 0  #variavel tentativas que vai receber o numeros de loops do código.

while True: #usamos while true para um loop infinito, enquanto for verdadeiro repita as instruçoes.

    palpite = int(input("Digite o palpite: "))# variavel palpite com uma entrada de dados do usuario.
    tentativas += 1 #soma +1 na var tentativas toda vez que o loop se repitir.

    if palpite < N_secret:# se palpite for menor que N_secret, mostre a mensagem na tela. assim o loop se repete.
        print("O numero é maior. Tente novamente!")

    elif palpite > N_secret: #aqui é a mesma lógica de if, por conta dessa condição ser true o while se repete.
        print("O numero é menor. Tente novamente!")#Mostra uma saida para o usuario.

    else: #Se todas as instruçoes acima for falsa o código deve se encerrar aqui (Else).
        print(f"Parabens voçê acertou o palpite em {tentativas} tentavias. \no numero é {N_secret}!")

        break #Por ser um loop infinito e as instruções do  código de (while true) for falso, 
            #para encerrar o loop utilizamos o breake.



"""
Solicita ao usuario N numeros, e soma eles. Se o usuario digitar 0 ele sai do programa e mostra o total da soma.
"""
soma = 0 

numeros = int(input("Digite um numero: "))

while numeros != 0:

    soma += numeros

    numeros = int(input("Digite um numero: "))

print(f"Total: {soma}")


#Pedindo uma lista de numeros para o usuario e mostrando o maior numero da lista.

numeros_int = int(input("Digite um numero inteiro: "))
N = []

while numeros_int > 0:

    print(numeros_int)

    numeros_int = int(input("Digite um numero inteiro: "))

    N.append(numeros_int)

    if numeros_int <= 0:

        maior = max(N)
        print(f"O maior numero é {maior}")

        break

#Corrigindo o codigo  acima 

N_list = []

num = int(input("Digite um numero: "))

while num > 0:
    N_list.append(num)

    print(num)
    num = int(input("Digite um numero: "))

Maior = max(N_list)
print(f"O maior numero é {Maior}")












    





    