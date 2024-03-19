#Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

lista = ["laranja","cerveja","miojo","carvão","picanha"]

produto = input("Escolha um item da loja: [laranja/cerveja/miojo/carvão/picanha]: ")

if produto in lista:
    print("Pode se dirigir ao caixa!")
else:
    print("Esse item não está disponível!")