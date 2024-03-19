#Faça um programa que receba dois valores A e B. Faça a potência desses dois valores e retorne o resultado:
#a ^ b = z

a = int(input("Insira um valor: "))
b = int(input("Insira outro valor para potencializar o primeiro: "))

resultado = pow(a,b)

print(a,"^",b," = ",resultado)