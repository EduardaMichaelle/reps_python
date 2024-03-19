#Faça um programa que receba um número. Verifique se este número é primo ou não, e retorne o resultado:

	#O número x é primo
#ou
	#O número x não é primo

numero = int(input("Digite um número: "))

#Números iguais ou menor que 1 não são primos
if numero < 2:
    print("Número não é primo!")

else: 
    #Verifica se o número é divisível por algum número de 2 até a metade do mesmo número
    for i in range(2, (numero//2 + 1)):
        if numero % i == 0:
            print("O número", numero, "não é primo.")
            break
    else:
        print("O número",numero,"é primo.")
    