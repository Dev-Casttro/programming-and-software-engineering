"""
Vai ser um sistema que á cada 1 real gasto no CPF do cliente, ele acumula pontos e
troca por descontos ou brindes.

requisitos 

Cadastro do cliente 
Armazenar esses dados
cliente deve fornecer o cpf 
Mostra a quantidade de pontos acumulados.

requisitos funcionais

cadastro do cliente - O sistema deve permitir que o cliente digite seus dados como Nome e cpf

Armazenar esses dados - O sistema deve armazenar esses dados para validar o cadastro.

cliente deve fornecer o cpf - O sistema deve compara os dados após o cliente digitar o cpf e valida, caso não seja 
os dados corretos ele invalida o cadastro e os pontos não acumula.

mostra a quantidade de pontos acumulados - O sistema deve mostrar a quantidade de pontos acumulados em toda compra.


"""
 
 # Sistema para cadastro

nome = []  #armazena os nomes 
cpf = [] #armazena os cpf 

while True: # continua o loop enquanto verdadeiro
    
    Nome_cadastro = input("Nome: ") # Solicita o nome do user.
    nome.append(Nome_cadastro)      # Adiciona o nome na lista nome.

    while True: # cria um loop 
     
        cpf_cadastro = (input("CPF: ")) # solicita o CPF para cadastro

        if len(cpf_cadastro) != 11: # verifica se o cpf tem menos que 11 elementos
            print("CPF Incorreto")  # se verdade, exibi a mensagem e retorna o loop
        else: 
            cpf.append(cpf_cadastro) # se if for falso, adiciona o cpf na lista 
        
            break  # encerra o loop.

    print ("Cadastro Realizado com Sucesso!")  # exibi a mensagem na tela.

    
    
    break

print()

# Sistema do Caixa

Pontos = 0 # Pontos do cliente 

print("Passe sua Compra e acumule pontos")

cliente = input("Digite o CPF: ") # solicita o CPF, caso cliente fidelizado

if cliente in cpf: # Compara se o CPF digitado é o mesmo que o cadastrado.
    print(f"\n{nome}") # exibi o nome do informado com cpf
    print(f"Pontos: {Pontos}")
else:
    print("CPF Invalido") # se if for falso, ele imprime cpf invalido.


# Processamento da compra 

import random

produtos_compra = float(random.randrange(1, 1500))

print(f"Total da compra: {produtos_compra}\n")




menu_pagamento = {

    1 : "Débito",
    2 : "Crédito",
    3 : "Dinheiro"
}

print("Formas de Pagamento\n"
      
      "1 - Débito\n"
      "2 - Crédito\n"
      "3 - Dinheiro\n"
      )

opcao_pagamento = int(input("Escolha a opção de pagamento (1-3): "))
menu_pagamento[opcao_pagamento]


if opcao_pagamento == 1 in menu_pagamento:

        Pontos = produtos_compra
        print(f"\n Pagamento Realizado com sucesso !\nPontos acumulados: {Pontos}\n")
    
elif opcao_pagamento == 2  in menu_pagamento:
   
        Pontos = produtos_compra
        print(f"\n Pagamento Realizado com sucesso !\nPontos acumulados: {Pontos}\n")
    
elif opcao_pagamento == 3  in menu_pagamento:

        Pontos = produtos_compra
        print(f"\nPagamento Realizado com sucesso !\nPontos acumulados: {Pontos}\n")
    
print("Obrigado por sua preferencia!")
    





    





