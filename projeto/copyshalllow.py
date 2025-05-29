d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],

}

#isto e uma copia raza, ela copia todos as chaves e valores da outra\
#porem quando dentro da outra ha subtipos alteraveis ele apenas linka os valores

d2 = d1.copy()
d2['c1'] = 1000
d2['l1'][0] = 1996
print(f'{d2} Vemos que d2 tem o valor de 1000')
print(f'{d1} Vemos que d1 nao recebeu o valor de 1000 mas' \
      ' recebeu o valor da lista que foi alterado no "d2"')