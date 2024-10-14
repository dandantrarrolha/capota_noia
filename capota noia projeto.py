import time

# isso define o tempo de delay
delayzinho = 1

def sauda():
    while True:  # Loop para repetir até que um nome válido seja fornecido
        print("Bem vindo ao sistema")
        name = input("Digite seu nome: ")
        
        if name.strip():  # Verifica se o nome não está vazio
            print("Bem vindo,", name + "!")
            break  # Sai do loop se um nome válido for fornecido
        else:
            print("Por favor, digite um nome válido.")

def menu():
    print("Como posso ajudar?")
    time.sleep(delayzinho)
    print("1 - Lanches")
    time.sleep(delayzinho)
    print("2 - Bebidas")
    time.sleep(delayzinho)
    print("3 - Sobremesas")
    time.sleep(delayzinho)
    print("0 - Sair")
    
    opcao = int(input("Digite o número da opção selecionada: "))
    return opcao

def escolher_lanche():
    print("Qual lanche você gostaria?")
    print("1 - Hotdog")
    print("2 - X-Salada")
    print("3 - Hamburguer")
    return int(input("Digite o número da opção selecionada: "))

def escolher_bebida():
    print("Qual bebida você gostaria?")
    print("1 - Milkshake")
    print("2 - Suco")
    print("3 - Refrigerante")
    return int(input("Digite o número da opção selecionada: "))

def escolher_sobremesa():
    print("Qual sobremesa você gostaria?")
    print("1 - Torta")
    print("2 - Bolo")
    print("3 - Churros")
    return int(input("Digite o número da opção selecionada: "))

def tks(pedido, categoria):
    if categoria == "lanche":
        if pedido == 1:
            print("Obrigado pela escolha do Hotdog.")
        elif pedido == 2:
            print("Obrigado pela escolha do X-Salada.")
        elif pedido == 3:
            print("Obrigado pela escolha do Hamburguer.")
    elif categoria == "bebida":
        if pedido == 1:
            print("Obrigado pela escolha do Milkshake.")
        elif pedido == 2:
            print("Obrigado pela escolha do Suco.")
        elif pedido == 3:
            print("Obrigado pela escolha do Refrigerante.")
    elif categoria == "sobremesa":
        if pedido == 1:
            print("Obrigado pela escolha da Torta.")
        elif pedido == 2:
            print("Obrigado pela escolha do Bolo.")
        elif pedido == 3:
            print("Obrigado pela escolha do Churros.")
    else:
        print("Opção incorreta. Digite uma das opções disponíveis.")   

def main():
    sauda()
    while True:
        opcao = menu()
        if opcao == 0:
            print("Saindo do sistema. Até logo!")
            break
        
        if opcao == 1:
            pedido = escolher_lanche()
            tks(pedido, "lanche")
        elif opcao == 2:
            pedido = escolher_bebida()
            tks(pedido, "bebida")
        elif opcao == 3:
            pedido = escolher_sobremesa()
            tks(pedido, "sobremesa")
        else:
            print("Opção incorreta. Digite uma das opções disponíveis.")

if __name__ == "__main__":
    main()