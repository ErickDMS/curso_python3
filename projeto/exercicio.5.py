cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10
resultado = 0
resultado2 = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo

resultado2 = resultado % 11
if resultado2 > 9 :
    resultado2 = 0
else:
    resultado2 = resultado % 11
print(f'O primeiro numero do cpf e {resultado2}')