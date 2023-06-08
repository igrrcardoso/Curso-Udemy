""" while/else """
string = 'Valor Qualquer '

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1

else:
    print('linha do else')
print('fora do else')
