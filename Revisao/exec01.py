"""Exercicio:
Peca ao usuario para digitar: Nome e idade.
Se nome e idade forem digitados:
    Exiba: Seu nome é {nome}
    Seu nome invertido é {nome_inevrtido}
    Se nome contém ou nao espacos
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}

Se nada for digitado em nome ou idade:
    exiba "Desculpe, voce deixou campos vazios"""
    
entrada = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if entrada  and idade:
    print(f"Seu nome é {entrada}")
    print(f"Seu nome invertido é {entrada [::-1]}")
    
    if " " in entrada:
        print("Seu nome contém espacos!")
    else:
        print("Seu nome nao contém espacos!")
        
    print(f"Seu nome tem {len(entrada)} letras")
    print(f"A primeria letra do seu nome é {entrada[0]}")
    print(f"A última letra do seu nome é {entrada[-1]}")
    
else:
    print("Desculpe, voce deixou campos vazios!")



