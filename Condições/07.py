#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Entre com uma palavra qualquer: ")
cont = 0

for i in palavra:
    if i == 'a':
        cont+=1

print(cont)