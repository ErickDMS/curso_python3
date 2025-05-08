entrada = 20
entrada_int = int(entrada)

print(f'entrada_int e {entrada_int}')

while entrada_int <= 80:
    print(f'Valor {entrada_int}')
    entrada_int += 1
    if entrada_int == 40:
        print('??')
        continue
    if entrada_int >= 50 and entrada_int <=60:
        print('??')
        continue

qtd_coluna = 5
qtd_linha = 5

linha = 1

while linha <= qtd_linha:
    coluna = 1
    while coluna <= qtd_coluna:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
