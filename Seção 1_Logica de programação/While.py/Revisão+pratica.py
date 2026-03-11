# O que é um while ?

"""
É um comando que usamos para criar um laço de repetição (loop).

Onde passamos uma condição para uma condição paera nosso programa, se for true ele executa,
senão ele encerra o laço.

exemplo:

enquanto o sinal estiver verde pode avançar, quando chegar no vermelho pare !
"""

cont = 1

while cont <= 10:
    print(cont)
    cont += 1

print()

"""
Aqui ele irá imprimir de 0 á 9, mas porque se eu coloquei 10 ?

O segredo está na regra de Sinais, se colocamos < 10, ele entende para contabilizar apenas os numeros menor que 10
apartir de 0,  a saída será de 0 a 9 contabilizando os numeros menor que 10. ok !

Agora se adicionarmos <= 10, ele entende para contabilizar os numeros menor que 10 só que
por conta do sinal de = ele se pergunta, 9 é menor-igual á 10 ?

É menor que 10, mas não é igual a 10, pela regrinha ele contabiliza o 10 
deixando de 0 á 10.

Entenda assim; Se voçê deixar < ele imprimi só os numeros menor que 10.
               Se voçê deixar <= ele imprimi os numeros menor e adiciona o 10.
"""

#while dentro de outro While 

#exercicio - historico de notas escolar 

import random

aluno_1 = "Willian"
aluno_2 = "Brendon"
aluno_3 = "Maikey"



print()

linha = 1

while linha <= 3:
    print()

    n1 = random.randrange(4,10)
    n2 = random.randrange(4,10)
    n3 = random.randrange(4,10)
    
    print()

    coluna = 0

    while coluna < 1:
        print(f"Notas do {linha}º SEMESTRE")
        print(f"\nNOME: {aluno_1} --- NOTA: {n1}\nNOME: {aluno_2} --- NOTA: {n2}\nNOME: {aluno_3} ---- NOTA: {n3}")
        
        

        coluna += 1
    
    linha += 1

