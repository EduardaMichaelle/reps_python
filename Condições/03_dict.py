#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago
#UTILIZANDO DICIONÁRIOS PARA ELIMINAR OS IF'S

escolha_tipo = input("Escolha um tipo de sorvete:  [casquinha/cascão/cestinha]: ").lower() #.lower() -> para quebra do case sensitive
escolha_sabor = input("Escolha o sabor do sorvete: [morango/creme/chocolate]: ").lower() 
escolha_cobertura = input("Escolha a cobertura do sorvete: [caramelo/morango/chocolate/sem cobertura]: ").lower()

valor = 0

sorvetes = {
    "casquinha": 1.00,
    "cascão": 2.50,
    "cestinha": 4.00
}

if escolha_tipo in sorvetes:
    valor += sorvetes[escolha_tipo]
else:
    print("Entre com um valor válido!")

coberturas = {
    "morango": 1.5, 
    "caramelo": 1.5, 
    "chocolate": 1.5,
    "sem cobertura": 0
}

if escolha_cobertura in coberturas:
    valor += coberturas[escolha_cobertura]
else: 
    print("Entre com um valor válido!")

print("Valor a ser pago: R$", valor)