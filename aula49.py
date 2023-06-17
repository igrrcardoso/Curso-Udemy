"""
Cuidado com os dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Igor', 1, True, False, 1.5, 999, 'Stalker']
lista_b = lista_a.copy()
lista_a[0] = 'Pripryat'
print(lista_a)
print(lista_b)
