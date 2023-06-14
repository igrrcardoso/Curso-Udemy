# texto = 'Python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i])

#     i += 1

texto = 'Python'
nova_string = ''
for letra in texto:
    print(letra)
    nova_string += f'*{letra}'

print(nova_string + '*')
