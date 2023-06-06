"""
Repetições 
While(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim.
"""
import os

condicao = True

while condicao:
    nome = input('digite seu nome: ')
    print(f'seu nome é {nome}')
    
    if nome == 'sair':
        os.system('cls')
        break