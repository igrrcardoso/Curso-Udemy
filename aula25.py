# interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - hexadecimal (ABCDEF0123456789)

nome = 'igor'
preco = 2137.96432
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %05X' % (1226, 1226))