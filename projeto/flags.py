condicao = False
passou_no_if = None

if condicao == True:
    passou_no_if = True
    print('Faca algo')
else:
    print('Faca nada')

if passou_no_if is None:
    print('Nao passou no if')
else:
    print('Passou no if')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)