"""
Interpolacao basica de strings
s - string
d e i - int
f . float
x e X - Hexadecimal (ABCDEF012345678)"""

nome ="Renato"
preco = 1000.95897643

variavel = "%s, o preco é R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %04x" % (15, 15))