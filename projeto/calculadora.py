
while True:

    numero1 = input('Digite um numero: ')
    numer02 = input('Digite outro numero: ')
    operador = input('Escolha o operador + - * /:')
    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero1)
        num2_float = float(numer02)
        numeros_validos = True
    except:
        if numeros_validos is None:
            print('Um dos numeros e invalido')
            continue

    operador_permitido = '+-*/'

    if operador not in operador_permitido:
        print('Operador invalido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '*':
        resultado = num1_float * num2_float
        print(f'Resultado: {resultado}')
    elif operador == '+':
        resultado = num1_float + num2_float
        print(f'Resultado: {resultado}') 
    elif operador == '-':
        resultado = num1_float - num2_float
        print(f'Resultado: {resultado}')   
    elif operador == '/':
        resultado = num1_float / num2_float
        print(f'Resultado: {resultado}')
    else:
        print('Algo de errado nao esta certo.')

    print('________________________')

    sair = input('Voce quer sair? [s]').lower().startswith('s')
    if sair:
        print('Good bye')
        break
    else:
        print('________________________')
