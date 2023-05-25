#nome = input('Qual seu nome?')
#print(f'o seu nome é {nome}')

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')       

    if not numero_1.isdigit() or not numero_2.isdigit:
        print('por favor, digite apenas números')


    elif numero_1.isdigit() or numero_2.isdigit():
        int_numero_1 = int(numero_1)
        int_numero_2 = int(numero_2)
        print(f'o resultado é: {int_numero_1 + int_numero_2}')

    else:
        print('você digitou algo além de números, por favor digite apenas')    

