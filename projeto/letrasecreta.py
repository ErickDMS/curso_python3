import os

p_secreta = 'Estudar'
l_acertadas = ''
num_tentativas = 0


while True:
    letra_digt = input('Digite uma letra: ')
    num_tentativas += 1
    
    if len(letra_digt) > 1:
        print('Digite apenas uma letra.')
       
        continue
    
    if letra_digt in p_secreta:
        l_acertadas += letra_digt
    
    p_formad = ''
    for letra_secret in p_secreta:
        if letra_secret in l_acertadas:
            p_formad += letra_secret

        else:
            p_formad += '*'
    print('Palavra formada: ', p_formad)

    if p_formad == p_secreta:
        os.system('clear')
        print(f'Voce ganhou, a palavra e ', p_formad)
        print(f'Numero de tentantivas = {num_tentativas}x')
        l_acertadas = ''
        num_tentativas = 0
