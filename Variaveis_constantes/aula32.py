"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = "ímpar"
    
    if par_impar:
        par_impar_texto = "Par"
    
    print(f"O número {numero_int} é {par_impar_texto}")
    
else:
    print("Vcoe nao digitou um número inteiro")
    

    
   
    