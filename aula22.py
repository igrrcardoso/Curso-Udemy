#operadores lógicos 
# and (e) or (ou) not (não)
# or - qualquer condição verdadeira avalia toda a expressão como verdadeira
# se qualquer expressão for validada como verdadeira,
# toda a expressão sera avaliada naquele valor
#são considerados falsy(que você já viu)
#0 0.0 '' False
#também existe o tipo none que é usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('digite a senha: ')
# senha_permitida = '123'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrando')
# else:
#     print('saindo')

#avaliação curto-circuito
# print(False or 0 or 'sb' or True)
# senha = input('senha: ') or 'sem senha'
# print(senha)
