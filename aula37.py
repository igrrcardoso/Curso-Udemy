"""
Repetições 
While(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim.
"""
import os

contador = 0 

while contador < 100:
    contador += 1
    print(contador)

    if contador > 8 and contador < 56:
        continue

    if contador == 60:
        break

print('fim do codigo') 
   


    