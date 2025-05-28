
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

multiplicado = input('Digite um numero: ')
multiplicado_int = int(multiplicado)

print(duplicar(multiplicado_int))
print(triplicar(multiplicado_int))
print(quadriplicar(multiplicado_int))
