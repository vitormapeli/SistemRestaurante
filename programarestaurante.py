# # import os

# opc = 0

# while (opc != 9):
#     print("MENU PRINCIPAL")
#     print("1. Cadastrar Restaurante")
#     print("2. Listar Restaurante")
#     print("9. Sair/Finalizar")

#     opc = int(input("ESCOLHA SUA OPÇÃO"))

#     match opc:
#         case 1: 
#             print("teste")
#             pausa = input("")
#         case 2: 
#             print("teste")
#             pausa = input("")
#         case 9: 
#             print("saida realizada")
#             pausa = input("")

# ========================================================
# PARTE 2
# ========================================================

import os

opc = 0


restaurante = ['Pizza', 'Cebola']

def novorestaurante():
    os.system('cls')
    print("Cadastrar novo restaurante")
    nome = input("Digite o nome do restaurante: ")
    restaurante.append(nome)
    pause = input("\n digite algo para continuar...")

def listarrestaurante():
    os.system('cls')
    for x in restaurante:
        print(x)
    pausa = input("\n digite algo para continuar...")


    

def menu():
    os.system('cls')
    print("MENU PRINCIPAL")
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Remover Restaurante")
    print("9. Sair/Finalizar")
    

def opcaoinvalida():
    print("Opção invalido...")
    input("digite algo para retornar")

def removerrestaurante():
    nomeremover = input("Insira o nome do restaurante a ser removido: ")
    restaurante.remove(nomeremover)

def opcoesMenu():
    try:
        opc = int(input("ESCOLHA SUA OPÇÃO: "))
        
        match opc:
            case 1: 
                novorestaurante()
            case 2: 
                listarrestaurante()
            case 3:
                removerrestaurante()
            case 9: 
                finalizarprograma()
                return opc  # Adicionando o retorno de opc caso a opção seja 9
                
            case _:
                opcaoinvalida()
    except ValueError: 
        opcaoinvalida()


def finalizarprograma():
    print(".")
    print("..")
    print("...")
    input("Digite algo para finalizar")
    exit()  # Adicionando a função exit() para finalizar o programa

while (opc != 9):
    menu()
    opc = opcoesMenu()

            
        
