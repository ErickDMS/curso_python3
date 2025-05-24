#primeiro escopo
x = 1
#posso usar global para definir x como uma variavel global
def escopo():
    x = 10
    def outro_escopo():
        y = 2
        print (y+x)
    outro_escopo()
    print(x)
print(x)
escopo()