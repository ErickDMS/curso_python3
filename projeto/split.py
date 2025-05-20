#lista_frase = frase.split(',')
#lista_frase = frase.split(', ') podem ser escritas assim para separar quando
#houver estes sinais

frase = "    O bagulho e doido e o bonde e sinistro, ta ligado?    "

lista_frase_fixa= frase.split()

lista_frase = []

for i, frase in enumerate(lista_frase_fixa):
    lista_frase.append(lista_frase_fixa[i].strip())

print(lista_frase)
print(lista_frase_fixa)\

frases_join = '-'.join(lista_frase)
print(frases_join)