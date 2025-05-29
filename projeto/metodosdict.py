# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Erick',
    'sobrenome': 'Santos',
    'idade': 30,
}

pessoa.setdefault('idade', 0)#adiciona valor se a chave não existe, caso exista faz nada
print(pessoa['idade'])
print(len(pessoa)) #quantas chaves
print(list(pessoa.keys())) #iterável com as chaves
print(list(pessoa.values())) #iterável com os valores
print(list(pessoa.items())) #iterável com chaves e valores

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)