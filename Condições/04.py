#Faça um programa que verifique se a pessoa pertence à família “calvo”.

nome = input("Entre com o seu nome: ") 
nome = nome.lower()

print(nome)

if 'calvo' in nome:
    print("Você pertence a família Calvo!")
else:
    print("Você não pertence a família Calvo...")