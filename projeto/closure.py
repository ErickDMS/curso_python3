"""
Closure sao funcoes que retornam outras funcoes
"""

def criar_saldacao(saldacao):
    def saldar(nome):
        return f'{saldacao}, {nome}'
    return saldar

bom_dia = criar_saldacao('Bom dia')
boa_noite = criar_saldacao('Boa noite')


for nome in ['Erick', 'Lais', 'Ozy']:
    print(bom_dia(nome))
    print(boa_noite(nome))