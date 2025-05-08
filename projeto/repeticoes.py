entrada = input('Digite um numero:')
entrada_int = int(entrada)

print(f'entrada_int e {entrada_int}')

while entrada_int <= 90:
    entrada_int=entrada_int + 1
    print('Acrescentado mais 1')
    print(f'Valor atual {entrada_int}')