# variáveis e exercicios 

# Ás variáveis diferençiam letras minusculas das maiusculas 

i = 30
I = "gusta"
print(i)
print(I)

# Podemos atribuir valores a varias variáveis em uma só linha 
"""
O código está utilizando o desempacotamento de tuplas (tuple) para atribuir varias variaveis 
em uma unica linha e, em seguida imprimindo essas variáveis.

A variavel var1 é atribuida a string "texto1"
var2 a string "texto2" e assim por diante.
"""
var1, var2, var3 = "texto1", "texto2", "texto3"
print(var1, var2, var3)

#Se tiver uma coleção de valores em uma lista, podemos extrair em variáveis. Isso é chamado de descompactar.

exemplo = "texto1", "texto2", "texto3"
var1, var2, var3 = exemplo
print(var1, var2, var3)

#EXERCICIOS 1

#1 Declare uma variavel chamada "idade" e atribua o valor 25 a ela

Idade = 25
print(Idade)

#2 Declare uma variavel chamada "Nome" e atribua um valor chamado "joão" a ela 

nome = "joão"
print(nome)

#3 Declare uma variavel chamada "saldo" e atribua o valor 100.50 a ela 

Saldo = 100.50

#4 Declare uma variavel chamada "soma" e atribua a ela a soma das variaveis "idade e saldo"

soma = Idade + Saldo

#5 imprima na tela o valor da variavel "soma"

print(soma)

#EXERCICIOS Bonus

#calculando a media da turma 

nota1 = 7.5
nota2 = 8.3
nota3 = 6.9

soma = nota1 + nota2 + nota3
media = soma / 3 
print (format(media, ".2f")) # para imprimir o valor com duas casas decimais utilizamos (FORMAT(..., ".2f"). 
