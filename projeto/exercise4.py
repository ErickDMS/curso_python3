frase = ' O Python e uma linguagem de programacao '\
    'multparadgma '\
    'criada por Guido Van Rossum'
i = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_apareceu = frase.count(letra_atual)
    print(letra_atual, quantas_vezes_apareceu) 
    
    i+= 1