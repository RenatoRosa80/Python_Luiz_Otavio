"""
Introdução ao empacotamento e desempacotamento
"""
nome1, nome2, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome2)

_, _, nome, *resto = ["Maria", "Helena", "Luiz"]
print(nome)

_, _, nome, *resto = ["Maria", "Helena", "Luiz"]
print(nome, resto)