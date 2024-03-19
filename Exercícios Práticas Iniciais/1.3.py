#Faça um programa que receba o raio de uma circunferência em centímetros. Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.
#Área:  x.xx
#Perímetro:  y.yy 
import math

raio = float(input("Entre com o valor do raio de uma circunferência em centímetros: "))

area = math.pi * (raio ** 2)
perimetro = 2 * math.pi * raio

print("Área:","{:.2f}".format(area),"\nPerímetro:","{:.2f}".format(perimetro))
