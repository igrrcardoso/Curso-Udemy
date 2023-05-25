while True:

    primeiro_valor = int(input('Digite o primeiro valor: '))
    segundo_valor = int(input('Digite o segundo valor: '))


    if primeiro_valor < segundo_valor:
        print(f'{primeiro_valor} é menor que {segundo_valor}')
    elif primeiro_valor > segundo_valor:
        print(f'{primeiro_valor} é maior que {segundo_valor}')
    elif primeiro_valor == segundo_valor:
        print(f'{primeiro_valor} é igual a {segundo_valor}')