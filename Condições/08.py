#Faça um programa que receba 4 alturas, armazene em uma lista e depois mostre a soma dessas alturas.

alturas = []

for i in range(4):
    a = int(input(f"Entre com a altura {i+1}: "))
    alturas.append(a)


soma = sum(alturas)
print(soma)