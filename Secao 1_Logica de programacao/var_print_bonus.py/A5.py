#imprimindo a posição da letra 

posicaoletra = "python"
print(posicaoletra[0])
print(posicaoletra[1])
print(posicaoletra[2])
print(posicaoletra[3])
print(posicaoletra[4])
print(posicaoletra[5])

#Slicing

#Obtendo uma parte da String usando Slice 
frase = "Olá, Mundo"
parte = frase[4:8]
print(parte) # Saída vai ser o "Mun", onde ele conta a partir da quarta letra 

#Obtendo os 4 primeiros caracteres da String 
primeiros = frase[:4]
print(primeiros) 
"""
Saída vai ser "Olá," contabilizando os 4 primeiros, se colocar o 5 primeiros vai sair "Olá, 
porque o python contabiliza o espaço entre uma letra a outra.
"""

#Obtendo os 6 ultimos caracteres da String 
ultimos = frase[-6:]
print(ultimos)#Saída vai ser "Mundo"

#Verifica se a palavra python está ma Frase 
Frase = "Python é legal"
print("Python" in Frase )

"""
O operador (in) é usado em python para verificar a presença de um valor dentro
de uma sequençia (como uma string, lista, ou tupla). Neste caso, está sendo usado para 
verificar se uma determinada substring está contida em uma string maior.
"""
#Split 
Frase = "Python é legal"

#if = se ...
if "Python" in Frase:
    print("Sim, a palavra Python está na frase")

# Usamos strip para remover espaços na frase no inicio e no final
Frase = "        Python é legal       "
print(Frase.strip())

#Strip e join são metodos muito uteis na string 
letras = "ólá, como vai vc ?"
palavras = letras.split()#Dividindo a frase em palavras usando o espaço em branco como separador 
print(palavras)

#join 
pallavras= ['1', '2', '3', '4',]
lettras = ''.join(pallavras)#Join ele junta os intens de uma lista 
print (lettras )#aqui juntamos com um espaço em branco 

# Strip remove sinais ou strings
texto = '**********Olá**********'
texto_strip = texto.strip('*')
print(texto_strip)

#remove os espaços em branco 
texto = '     Olá   '
texto_strip = texto.strip()
print(texto_strip)
