#serve para voce capturar o erro
numero_str = input('Vou dobrar o numero que voce digitar: ')

try:
    numero_float = float(numero_str)
    print(f'FLOAT', numero_float)
    print(f'O dobro de {numero_str} e {numero_float * 2:.2f}')
except:
    print('Isso nao e um numero')