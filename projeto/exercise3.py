
name = input ('Digite seu nome: ')
old = input ('Digite sua idade: ')
if (name and old):

    print(f'seu nome e {name}')
    print(f'seu nome de tras pra frente e {name[::-1]}')


    if ' ' in name:
        print('Seu nome contem espaco')
    else:
        print('Seu nome nao contem espaco')
    print(f'Seu nome tem {len(name)} letras')
    print(f'A primeira letra do seu nome e {name[0]}')
    print(f'A ultima letra do seu nome e {name[-1]}')
else:
    print('Desculpe voce deixou campos vazios')