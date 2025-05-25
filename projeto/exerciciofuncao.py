num = 1, 2, 3, 4, 5, 6

def mult(*args):
    
    total = 1
    
    for numeros in args:
        total = numeros * total
    
    return total
    
resultado = mult(*num)

print(resultado)


num2 = input('Digite um numero: ')

def par_impar(x):
    y = int(x)
    conta = y % 2
    if conta == 0:
        return f'{conta} Numero par'
    
    return f'{conta} Numero impar'
    

result = par_impar(num2)
print(result)