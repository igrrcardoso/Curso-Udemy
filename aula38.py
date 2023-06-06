"""
Repetições 
While(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim.
"""

qtd_linhas = 5
qtd_colunas = 6

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_linhas:
        print(f'{linha} {coluna}')
        coluna += 1
    linha += 1

print('fim')
