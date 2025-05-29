pessoa = {}

chave = 'nome'

pessoa[chave] = 'Erick'
pessoa['sobrenome'] = 'Santos'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])


if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])



