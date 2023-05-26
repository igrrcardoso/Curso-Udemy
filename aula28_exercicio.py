"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados 
Exiba : 
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contém (ou não) espaços
            Seu nome tem {n}
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é{letra}
        Se nada for digitado em nome ou idade:
         Exiba "Desculpe, você deixou campos vazios
"""


# variaveis
nome = (input('Digite seu nome: '))
idade = (input('Digite sua idade: '))
quantidade_letras = len(nome)
espacos = " "
ultima_letra = nome[:-1]
primeira_letra = nome[:1]
nome_invertido = nome [::-1]
#bloco if
if nome and idade != '':
    print(f'seu nome é {nome}')
    print(f'você tem {idade} anos de idade')
    print(f'Seu nome invertido é {nome_invertido}')
    print(f'seu nome tem {quantidade_letras} letras')
    print(f'a primeira letra do seu nome é {primeira_letra}')
    print(f'a última letra do seu nome é {ultima_letra}')
    if espacos in nome:
        print('Seu nome contém espaços')
    elif espacos not in nome:
        print('Seu nome não contem espaços')
else:
    print('Desculpe, você deixou campos vazios')



