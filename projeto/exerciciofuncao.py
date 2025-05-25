num = 1, 2, 3, 4, 5, 6

def mult(*args):
    
    total = 1
    
    for numeros in args:
        total = numeros * total
    
    return total
    
resultado = mult(*num)

print(resultado)