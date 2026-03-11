#xercicio - Calculadora de descontos 

#Solicita o valor da compra, usamos float para coversão e receber um valor númerico.
compra_valor = float(input("Insira o valor da compra: "))


if compra_valor > 1000: #verifica a condição para aplicar o desconto correto, acima de 1000 é 20% de desconto.

    mensagem = str("você recebeu 20% de desconto")
    print(mensagem.capitalize())#corrige o erro de escrita, converte a primeira letra para maiusculo 


    valor_desconto = compra_valor * 20 / 100 # var desconto recebe o valor e calcula a porcetagem para o desconto.
    total_valor = compra_valor - valor_desconto #var total recebe o calculo com o desconto aplicado.

    print(f"Desconto: {valor_desconto:.2f}")#mostra o valor do desconto com duas casas decimais.
    print(f"Total: {total_valor:.2f}")#mostra o valor total, com o desconto aplicado.

elif compra_valor >= 500 and compra_valor <= 1000: #verifica a condição para aplicar o desconto correto.
                                                   #compras entre 500 e 1000 é 10% de desconto 
    print("você recebeu 10% de desconto")       

    valor_desconto = compra_valor * 10 / 100 # var desconto recebe o valor e calcula a porcetagem para o desconto.
    total_valor = compra_valor - valor_desconto #var total recebe o calculo com o desconto aplicado.


    print(f"Desconto: {valor_desconto:.2f}")#mostra o valor do desconto com duas casas decimais.
    print(f"Total: {total_valor:.2f}")#mostra o valor total, com o desconto aplicado.

else:
    print(f"Compras abaixo de {compra_valor} não recebe desconto!")#comunica o cliente, se não tiver desconto.