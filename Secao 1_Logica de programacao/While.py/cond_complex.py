# Condições complexas com while.

# O exemplo abaixo demonstra um programa que incrementa 1 na variavel (x) até 10 e decrementa 1 na var (y) até 10.

x, y = 5, 15 

# O loop continuara enquanto ambas condições forem verdadeiras.
while x < 10 and y > 10: #Dica: Caso queira mostrar o numero 10 em ambos, é só adicionar o (=) que ele soma e subtrai mais 1.

    print(f"X: {x} --- Y: {y}") # primeiro imprimimos o valores iniciais com print.

    x += 1   # Somamos mais 1 em ambas as variaveis.
    y -= 1 

print("loop concluido com sucesso!")
print(f"Valores Finais: X = {x} -- Y = {y}") 

#Dica: colocamos os print com os resultados finais fora do processamneto das instruções.
# dentro do no while agente processa informaçoes, e fora agente exibi os resultados das informaçoes ou criamos as info..

print()

num_secret = 7
num_secre2 = 3

tentativas = 5 

adv1 = False
adv2 = False

while tentativas > 0 and ( not adv1 == True or not adv2 == True): # Se essas instruções for true ele executa o proximo.

    print(f"tentativas restantes: {tentativas}") # Imprime a mensagem 

    palpite1 = int(input("Digite seu primeiro palpite entre (1- 10): ")) # solicita um dado com comando de entrada input.
    palpite2 = int(input("Digite seu segundo palpite entre (1- 10): ")) # solicita um dado com comando de entrada input.

    if palpite1 == num_secret:              # Se palpite1 for igual a num_secret -> imprima a mensagem.
        print(f"Voçê adivinhou o primeiro número secreto!")

        adv1 = True                 # Aqui ele muda o status da variavel para true. 

    if palpite2 == num_secre2:           # Se palpite2 for igual a num_secret -> imprima a mensagem.
        print(f"Voçê adivinhou o segundo número secreto!")

        adv2 = True                 # Aqui ele muda o status da variavel para true. 

    if not adv1 == True or not adv2 == True: # se adv1 e adv2 permanecer false, ele imprime a mensagem.

        print("Tente novamente!")

        tentativas -= 1  #decrementa 1 na variavel tentativas.

if adv1 and adv2: # Se adv1 e adv2 for true ele pula e imprime a mensagem encerrando o programa.

    print("Parabens! Voçê adivinhou os números secretos.")

else: # caso adv1 e adv2 seja false ele imprime a mensagem e encerra o programa.
    print(f"Voçê não conseguiu adivinhar os números secretos! Eles eram {num_secret} e {num_secre2}")


# Explicando a estrutura e a lógica

"""
 . Declaramos nossa variavel fora do loop (while), porque queremos elas imutaveis.
 
 . Dentro do loop agente solicita ao usuario, e processa as informaçôes.
 
 . Aqui não usamos o elif por conta que; O elif ele só é processado caso a primeira condição (if) seja falsa, 
e como queremos testar a segunda condição independente se é true ou false, usamos (if) ao invés de (elif).
 
 . Fora do loop (while) colocamos nossas definições, dentro do loop processa e fora defini. Queremos definir que, 
 se o processamento das informaçoes forem verdadeiras e mudar nosso status da variaveis para true exibi uma mensagem.
 
 . Caso seja ao contrario e nosso usuario esgotar o numeros de tentativas, o loop se encerra e defini com else fora 
 do nosso comando while imprimindo a mensagem.


"""

n = 10  # Altere esse valor para calcular a soma de diferentes quantidades de números ímpares

contador = 0
soma = 0
numero_impar_atual = 1

while contador <= n:
    soma += numero_impar_atual 
    numero_impar_atual += 2 
    contador += 1 
    
    print(soma)

