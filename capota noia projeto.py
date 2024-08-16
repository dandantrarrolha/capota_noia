import time

# isso define o tempo de delay
delayzinho = 3;


# isso mostra uma mensagem inicial
print("Bem vindo ao sistema")


# isso vai pedir o nome do usuário
name  = input("Digite seu nome:")

print("Bem vindo,", name + "!")

time.sleep(delayzinho)

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


elif opcao == 2:
    print("Qual Bebida você gostaria?")   

elif opcao == 3:
    print("Qual Sobremesa você gostaria?") 

else:
    print("Opção incorreta. Digite uma das opções disponíveis")   