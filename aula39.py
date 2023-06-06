"""
iterando strings com while
"""

nome = 'Igor Cardoso'

indice = 0
separacao = "*"
while indice < len(nome):
    letra = nome[indice]
    separacao += f'{letra}*'
    indice += 1

print(separacao)
