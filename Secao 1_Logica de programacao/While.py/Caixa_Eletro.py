#desafio do caixa eletronico


Menu = {              # Dicionário para deixar o código mais organizado e para dar um significado para cada numero.
    1 : "Saldo", 
    2 : "Depósito",
    3 : "Sacar",
    4 : "Sair"
}

saldo = 1000       # criamos 4 variaveis do tipo inteiro para cada opção do menu, Saldo recebe 1000 para inicio do código e as demais zero.
depósito = 0       # As variaveis estão fora do loop por conta de serem valores fixos. Para não sofrer alteração e somarmos a cada transição.
sacar = 0          
sair = 0

while True:         # utilizei while True para o loop se repetir até que o usuario digite a opção sair(4).
        
        print("Caixa Eletronico\n" # Com print Criamos nosso menu representativo, para apenas mostra as opçoes para escolha do usuario.
        "1 - Saldo\n"              # Com \n fizemos o layout do menu.
        "2 - Depósito\n"           # Nosso código ja se inicia mostrando as opçoes para o usuario. assim com o menu vindo no topo do escopo.
        "3 - Sacar\n"
        "4 - Sair")
                
        opcão = int(input("Escolha uma opção de (1 - 4): ")) #Criamos uma saída para o usuario, com a variavel (opcão).
        print(Menu[opcão])                   # Aqui na linha 25. cada escolha irá consultar o dicionario e mostrar na tela a opção escolhida.

        if opcão == 1 in Menu:              # Usamos if para criar as instruções de cada opção do menu.
                print(f"Seu Saldo é de {saldo}\n") 
                
                """
                Aqui ele compara (1) e consulta o dicionario, 
                consulta a variavel (saldo = 1000) e  mostra o saldo na tela . """
        
        elif opcão == 2 in Menu:
                depósito = int (input("Digite o valor do depósito: \n"))
                saldo = saldo + depósito 
                print("Depósito realizado com sucesso!\n")

                """
                se a opçaõa escolhida for igual 2, compara e consulta o dicionario, depois utilizamos a nossa variavel depósito 
                para receber um valor inteiro e armazernar.

                para somar  e atualizar o saldo atual após o depósito, fizemos a variavel saldo receber ela mesma + o valor do depósito. 
                """

        elif opcão == 3 in Menu:
                sacar = float(input("Digite o valor do saque: \n"))

                if saldo < sacar:
                    print("Seu saldo é insuficiente!")
                        
                else:
                    saldo = saldo - sacar
                    print("Saque realizado com sucesso!\n")

                    """
                    Aqui se a opção escolhida for igual a 3, ele compara e consulta no dicionario. 
                    para o saque, a varial sacar vai exibir uma saída solicitando o valor para o saque.
                    
                    utilizamos float para armazernar o saldo negativo (0.00).

                    aqui está o pulo do gato! se o saldo for negativo ele mostra  seu é saldo é insuficiente.

                    caso o saldo seja seja pósitivo ele pula direto para a subtração do saldo e realiza a transição.

                    para essas duas condiçoes usamos if e else dentro do elif opção 3. 

                    """

      
                        
        else: 
            print("Obrigado por sempre escolher o PRAFRENTEX!") # caso ele escolha 4. o progrma exibi a mensagem e encerra.

            break
                        

                


    

    