""" *args e uma forma de chamar os argumentos sem precisar chamar cada um por seu nome
"""

tupla = 1, 2 ,3 ,4 ,5 ,6 ,7

def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(total, numero)


soma(*tupla)

## a funcao 'sum()' server para fazer essa soma acima
print (sum(tupla))