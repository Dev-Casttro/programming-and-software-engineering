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


    print(nome, cpf)

    





