"""
Faca uma lista de compras, com listas. O usuario deve ter a possibilidade de inserir,
apagar e listar valores da sua lista. Nao permita que o programa quebre 
com erros de indices inexistentes na lista"""
import os

lista = []

while True:

    print("Selecione uma opcao")
    opcao= input("[i]iserir, [a]pagar, [l]istar, [t]erminar:")
    
    if opcao == "i":
        os.system("cls")
        valor = input("Item: ")
        lista.append(valor)
    elif opcao == "a":
        indice_str = input("Escolha o item para apagar: ")  
        try:
            indice = int(indice_str)
            del lista[indice]      
        except ValueError:
            print("Nao foi possivel apagar o item desejado!")
        except TypeError:
            print("Por favor, digite um numero inteiro!")
    elif opcao == "l":
        os.system("cls")
        
        
        if len(lista) == 0:
            print("Nada para listar. ")
            
        for i, valor in enumerate(lista):
            print(i, valor)
            
    elif opcao == "t":
        print("Você terminou a sua lista! Até mais 👋")
        break

    else:
        print("Opção inválida, tente novamente!")
             
        
        