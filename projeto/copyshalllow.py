#aqui e uma importacao do metodo copy para copiar a fundo tudo do dicionario
import copy

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

d3 = copy.deepcopy(d1) #deepcpoy e um metodo para copiar todos os subniveis
d3['l1'][0] = 2025

print(f'{d3} Vemos que d3 copia tudo do d1 sem linkar, entao qualquer alteracao' \
      ' que seja feita nao vai afetar d1')