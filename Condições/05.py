#Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

nome = input("Entre com seu nome todo: ")
nome = nome.lower()

if 'calvo' in nome:
    print("Você pertence a família Calvo!")

else:
    print("Você não pertence a família Calvo...")

if 'silva' in nome:
    print("Você pertence a família Silva!")
else:
    print("Você não pertence a família Silva...")