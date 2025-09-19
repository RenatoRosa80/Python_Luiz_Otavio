"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = "Olha só que, coisa interessante"
lista_palavras = frase.split()
print(lista_palavras)

print("-----------------------------------")
frase = "Olha só que, coisa interessante"
lista_palavras = frase.split(",")
print(lista_palavras)

print("-----------------------------------")

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].lstrip()) # strip corta os espacos da esquerda. rstrip, corta o espaco da direita
    
print(lista_palavras)
    
