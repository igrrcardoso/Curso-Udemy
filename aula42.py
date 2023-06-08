frase = 'o python é uma linguagem de programação '\
    'multiparadigma'\
    'Python foi criado por Guido van Russom'

i = 0
qtd_apareceu_mais_x = 0
letra_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_x_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_x < qtd_apareceu_mais_x_atual:
        qtd_apareceu_mais_x = qtd_apareceu_mais_x_atual
        letra_mais_apareceu = letra_atual

    i += 1

print(
    'A letra que mais apareceu foi: '
    f'"{letra_mais_apareceu}"'
    f' {qtd_apareceu_mais_x}x'
)
