#Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago

valor_casquinha = 1.0
valor_cascao = 2.50
valor_cestinha = 4.0
valor_cobertura = 1.50

escolha_tipo = input("Escolha um tipo de sorvete:  [casquinha/cascão/cestinha]: ")
escolha_sabor = input("Escolha o sabor do sorvete: [morango/creme/chocolate]: ")
escolha_cobertura = input("Escolha a cobertura do sorvete: [caramelo/morango/chocolate/sem cobertura]: ")

if escolha_tipo == "casquinha":
    if escolha_sabor == "morango" or escolha_sabor == "creme" or escolha_sabor == "chocolate":
        if escolha_cobertura == "sem cobertura":
            print("Valor a ser pago: R$", valor_casquinha)
    
        elif escolha_cobertura == "caramelo" or escolha_cobertura == "morango" or escolha_cobertura == "chocolate":
            valor_total = valor_casquinha + valor_cobertura
            print("Valor a ser pago: R$", valor_total)
    
        else:
            print("Entre com uma escolha válida!")
    else:
        print("Entre com uma escolha válida!")

elif escolha_tipo == "cascão":
    if escolha_sabor == "morango" or escolha_sabor == "creme" or escolha_sabor == "chocolate":
        if escolha_cobertura == "sem cobertura":
            print("Valor a ser pago: R$", valor_cascao )
    
        elif escolha_cobertura == "caramelo" or escolha_cobertura == "morango" or escolha_cobertura == "chocolate":
            valor_total = valor_cascao + valor_cobertura
            print("Valor a ser pago: R$", valor_total)
    
        else:
            print("Entre com uma escolha válida!")
    else: 
        print("Entre com uma escolha válida!")

elif escolha_tipo == "cestinha":
    if escolha_sabor == "morango" or escolha_sabor == "creme" or escolha_sabor == "chocolate":
        if escolha_cobertura == "sem cobertura":
            print("Valor a ser pago: R$", valor_cestinha )
    
        elif escolha_cobertura == "caramelo" or escolha_cobertura == "morango" or escolha_cobertura == "chocolate":
            valor_total = valor_cestinha + valor_cobertura
            print("Valor a ser pago: R$", valor_total)
    
        else:
            print("Entre com uma escolha válida!")
    else:
        print("Entre com uma escolha válida!")

else:
    print("Entre com uma escolha válida!")