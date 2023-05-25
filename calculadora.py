#Teste calculadora 100% sozinho
print('bem-vindo à minha primeira calculadora, feita "100%" sozinho')
while True:

    numero_1 = float(input('Digite o primeiro número: '))
    operação = input('Selecione o operador "+, -, /, **, %, *": ')
    numero_2 = float(input('Digite o segundo número: '))

    if operação == ("+"):
        resultado = numero_1 + numero_2
    elif operação == ("-"):
        resultado = numero_1 - numero_2
    elif operação == ("/"):
        resultado = numero_1 / numero_2
    elif operação == ("**"):
        resultado = numero_1 ** numero_2
    elif operação == ('%'):
        resultado = numero_1 % numero_2
    elif operação == ('*'):
        resultado = numero_1 * numero_2

    print(f"o resultado é: {resultado:.2f} ")

    opcao = input('você deseja sair? "digite [s] ou [q]')
    if opcao == 's' or 'q':
        print('Obrigado por utilizar a calculadora, até!')
        break
        

