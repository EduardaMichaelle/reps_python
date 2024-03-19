numero_sorte = 7

for i in range(3): 

    while True:

        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            break
        except ValueError:  #erro de tipagem
            print("ERROR! Digite um número válido!")
            continue

    if numero == numero_sorte:
        print("Você acertou!")
        break
    elif numero > numero_sorte:
        print("Que pena, você errou! Tente um número menor.")
    else: 
        print("Que pena, você errou! Tente um número maior.")