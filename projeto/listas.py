lista = []
lista_teste = ['abc', 'defg']
while True:
    variavel1 = input('Digite um numero: ')
    lista = ['']
    lista[0] = variavel1
    variavel2 = input('Digite outro numero: ')
    lista += ['']
    lista[1] = variavel2
    print(lista)
    break
print('Outro meio de adicionar')
lista.append(50)## Adiciona no final
lista.pop()## Apaga o final ou um indice escolhido
lista.insert(0, 4) #adiciona algo em um indice selecionado
variavel3 = input('Digite mais algum numero: ')
if lista[1] < variavel3:
    lista.append(variavel3)
    print(lista)
lista.extend(lista_teste) ## uma forma de concatenar
print(lista)
lista_teste2 = lista.copy()
print('lista_teste2', lista_teste2)