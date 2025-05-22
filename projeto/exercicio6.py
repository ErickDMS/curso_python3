cpf = input ('Digite seu CPF: ')
nove_digitos = cpf[:9]
contador_regressivo = 10
resultado = 0

for digito in nove_digitos:

    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

digito1 = (resultado * 10)% 11

digito1 = digito1 if digito1 < 9 else 0


##Segundo numero

contador_regressivo2 = 11
resultado2 = 0
dez_digitos = cpf[:10]

for digito2 in dez_digitos:
    resultado2 += int(digito2) * contador_regressivo2
    contador_regressivo2 -= 1

digito2 = (resultado2 * 10)% 11

digito2 = digito2 if digito2 < 9 else 0
print(f'Os numeros correspodem ao calculo. {digito1}{digito2}')
