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
    result = 0
    conta = y % 2
    if conta == 0:
        result = 'Numero par'
    else:
        result = 'Numero impar'
    return result
    

result = par_impar(num2)
print(result)