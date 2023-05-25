#Operadores in e not in
# Strings são iteráveis 
# 0 1 2 3
# i g o r
# -4-3-2-1

# nome = 'Igor'
# print(nome[3])
# print(nome[-1])
# print('o' in nome)
# print('Ig' in nome)
# print('pri' in nome)
# print('a' in nome)

nome =input('digite seu nome: ')
encontrar = input('digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')



