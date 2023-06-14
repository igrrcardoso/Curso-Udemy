"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# texto = iter('Igor')  # __iter__()
# print(next(texto))  # __next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))

texto = 'igor'
iterator = iter(texto)

# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
    