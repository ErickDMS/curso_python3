entrada = input('Digite um numero inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    resultado = 'impar'
    if par_impar:
        resultado = 'par'
    print(f'O numero {entrada_int} e {resultado}')
else:
    print('Voce nao digitou numero inteiro')

###################################

entrada2 = input('Digite a sua hora: ')

try:
    hora = int(entrada2)
    if hora >= 0 and hora <= 11:
        print("Bom dia")
    elif hora >=12 and hora <= 17:
        print("Boa tarde")
    elif hora >=18 and hora <= 23:
        print("Boa noite")
    else:
        print("Nao conheco essa hora")

except:
    print("Por favor digite apenas numeros")

####################################

entrada3 = input('Digite seu nome: ')
tamanho_nome = len(entrada3)

if tamanho_nome > 1:
    if tamanho_nome<= 4:
        print('Seu nome e curto')
    elif tamanho_nome>= 5 and tamanho_nome <= 6:
        print('Seu nome e normal')
    else:
        print('Seu nome e muito grande')
else:
    print('Digite mais de 3 letras')