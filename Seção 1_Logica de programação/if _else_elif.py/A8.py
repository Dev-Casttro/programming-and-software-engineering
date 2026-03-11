#Se....or
#Se...ou

num1 = 19
num2 = 150
num3 = 18

if num1 > num2 or num3:
    print(f" O {num1} é maior que {num2} ou {num1} é maior que {num3}")


#EXERCICIO - entrada para um evento exclusivo

vip = input("Voçê é possui o convite VIP: ")# entrada de dados do usuario, pergunta com input.
lista_conv = input("Voçê está na lista de convidados: ")
membros_club = input("Voçê é membro do clube: ")

if vip == "sim" or lista_conv == "sim" or membros_club == "sim": #Se pelo menos uma das condições for true ele executa a msg.
    print(f"Bem - vindo(a) ao evento!")

elif vip == "não" or lista_conv == "não" or membros_club == "não": 
    print("Desculpe voçê não pode entrar no Evento!")

#Exercicio - Par ou Impar

n1 = int(input("Digite um número: "))
verif_num = n1 % 2 #Aqui o % pega o resto da divisão, 10 divido por 2 é 5, ou seja, restou nada (0).

if verif_num == 0: # Se o restante for 0, ou seja, divisivel por 2 é Par 
    print(f"{n1} é Par")

else:
    print(f"{n1} é Impar") # se não for divisivel e resta um valor é impar