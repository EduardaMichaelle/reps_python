#código da loteria, mas utilizando funções e bibliotecas

import random

def valida_entrada():

    while True:  
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))

        except ValueError:  #erro de tipagem
            print("ERROR! Digite um número válido!")
            continue #faz voltar para o começo do laço e tenta de novo antes de seguir com o resto do código

        if 1 <= numero <= 15:
            return numero
        else:
            print("Entre com um número válido!")

numero_sorte = random.randint(1,15)

for i in range(3): 

    numero = valida_entrada()

    if numero == numero_sorte:
        print("Você acertou!")
        break
    elif numero > numero_sorte:
        print("Que pena, você errou! Tente um número menor.")
    else: 
        print("Que pena, você errou! Tente um número maior.")


print("O número sorteado era:", numero_sorte)