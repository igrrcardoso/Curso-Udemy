"""
calculadora com while
"""
while True:
    numero1 = input('digite o primeiro número: ')
    numero2 = input('digite o segundo número: ')
    operador = input('digite o operador (+-*/): ')

    operadores_permitidos = "+-/*"
    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('você digitou um ou ambos números inválidos.')

    if operador not in operadores_permitidos:
        print('você digitou um operador inválido.')

    if len(operador) > 1:
        print('digite apenas um operador.')

# bloco if operadores

    if operador == "+":
        soma = num1_float + num2_float
        print(soma)
    elif operador == "-":
        subtracao = num1_float - num2_float
        print(subtracao)
    elif operador == "*":
        multiplicacao = num1_float * num2_float
        print(multiplicacao)
    elif operador == "/":
        divisao = num1_float / num2_float
        print(divisao)

    sair = input('você quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break