#Faça um programa que receba dois valores A e B. Faça a soma desses dois valores e retorne o resultado:
#Soma:  x.xx

a = float(input("Insira um valor: "))
b = float(input("Insira outro valor para somar ao primeiro: "))

soma = a + b

print(f"Soma = ","{:.2f}".format(soma))