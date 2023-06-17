"""
listas em Python
tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamentos
Métodos úteis:

    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista

Create Read Update Delete
Criar, ler, atualizar, deletar (CRUD)
"""

#         01234
#        -54321
# string = 'ABCDE'  # 5 caracteres

# lista = [455, 'Igor', 1.3, False, []]
# lista[1] = 'Cardoso'
# print(lista)

# lista = [10, 20, 30, 40]
# lista.append('Igor')
# nome = lista.pop()
# lista.append(888)
# del lista[-1]
# lista.clear()
# lista.insert(100, 999)

lista_a = [4, 5, 6]
lista_b = [7, 8, 9]
# lista_ab = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
