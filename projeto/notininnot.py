name = 'Erick'
print (name)
print ("r" in name)
print ("t" not in name)


nome = input("Digite o seu nome: ")
encontrar = input ("Digite o que voce quer encontrar: ")

if encontrar in nome:
    print (f'{encontrar} esta em {nome}')
else:
    print (f'{encontrar} nao esta em {nome}')