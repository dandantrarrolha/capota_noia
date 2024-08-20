import time

# isso define o tempo de delay
delayzinho = 1;


def sauda():

    # isso mostra uma mensagem inicial
    print("Bem vindo ao sistema")

    # isso vai pedir o nome do usuário
    name  = input("Digite seu nome:")

    print("Bem vindo,", name + "!")


def menu():

    print("Como posso ajudar?")

    time.sleep(delayzinho)

    print("1 - lanche")

    time.sleep(delayzinho)

    print("2 - Bebidas")

    time.sleep(delayzinho)

    print("3 - Sobremesas")

    opcao = int(input("Digite o número da opção selecionada:"))

    if opcao == 1:
        print("Qual lanche você gostaria?")
        print("1-hotdog")
        print("2-x-salada")
        print("3-hamburguer")

    elif opcao == 2:
        print("Qual Bebida você gostaria?")   
        print("1-milkshake")
        print("2-suco")
        print("3-refrigerante")
    elif opcao == 3:
        print("Qual Sobremesa você gostaria?")
        print("1-torta")
        print("2-bolo")
        print("3-churros")

    else:
        print("Opção incorreta. Digite uma das opções disponíveis")   


def tks():
    pedido = int(input("Digite o número da opção selecionada:"))

    if pedido == 1:
        print("obrigado pela escolha")

    elif pedido == 2:
        print("obrigado pela escolha")

    elif pedido == 3:
        print("obrigado pela escolha")

    else:
        print("Opção incorreta. Digite uma das opções disponíveis")   

sauda()
time.sleep(delayzinho)
menu()
tks()


