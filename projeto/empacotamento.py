##uma lista pode ser desempacotada dessa forma
## nome = ['Erick', 'David', 'Santos']
nome1, nome2, *resto = 'Erick', 'David', 'Santos'

print(resto)
## uma tuple e uma lista imutavel
## uma lista tuple se faz assim 
nome = 'erick', 'david', 'santos'
## ou pode ser feito isso
nome5 = ['erick', 'david', 'santos']
nome5 = tuple(nome5)
print(nome5)

##desempacotamento atravez de funcao
## pode ser ultilizado o '*' para interar todos os itens
print(*nome5, sep= '\n')
