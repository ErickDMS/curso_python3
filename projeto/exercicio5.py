import os

lista = []

while True:
    entrada = input('Escolha uma opcao [i]nserir, [a]pagar, [l]istar: ')
    if entrada == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif entrada == 'a':
        os.system('clear')
        print(f'A lista contem {len(lista)} itens')
        indice_str = input('Escolha o indice para apagar')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif entrada == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Voce nao escolheu nenhuma opcao valida')
