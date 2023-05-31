"""
introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input(
    'vou dobrar o número q vc digitou : '
    )
try:
    dobrar = float(numero) * 2
    print(f'{dobrar}')
except:
    print(f'Isso não é um número')
