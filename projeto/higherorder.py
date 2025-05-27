"""isso e para mostrar que com a funcao voce pode fazer varias coisas
incluindo usar funcao como parametro de outra e ate mesmo funcao em return"""


def saldacao(msg, nome):
    return f'{msg}, {nome}'

def executar(funcao, *args):
    return funcao(*args)

print (
    executar(saldacao, 'Bom dia', 'Erick')
)