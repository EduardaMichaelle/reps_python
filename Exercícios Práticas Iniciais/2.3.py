#Escreva um programa que solicite ao usuário um nome e uma idade, e crie um dicionário com essas informações. Em seguida, exiba o dicionário.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

dicionario = {"Nome": nome, "Idade": idade}

print(dicionario)