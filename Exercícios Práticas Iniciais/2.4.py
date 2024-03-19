#Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:

#Média: x
#Menor: y
#Maior: z

nota1 = int(input("Entre com a primeira nota: "))
nota2 = int(input("Entre com a segunda nota: "))
nota3 = int(input("Entre com a terceira nota: "))
nota4 = int(input("Entre com a quarta nota: "))

lista = [nota1,nota2,nota3,nota4]

maior=0 #auxiliar
for i in lista: #para cada nota na lista
    if i > maior: #se a nota for maior que a variável "maior"  
        maior = i #então a variável "maior" receberá o valor dessa nota

menor=maior #auxiliar recebe o valor da maior nota 
for i in lista: #para cada nota na lista
    if i < menor: #se a nota for menor que a variável "menor" (que inicialmente tem o valor da maior nota)
        menor = i #então a variável "menor" receberá o valor dessa nota 

media = (nota1 + nota2 + nota3 + nota4)/4

print("Média:",media)
print("Menor:",menor)
print("Maior:",maior)