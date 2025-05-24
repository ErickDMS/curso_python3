"""uma funcao nao pode retornar um valor como uma variavel,
para que isso seja possivel voce usa o comando 'return' assim
voce pode atribuir o valor da funcao diretamente para uma variavel"""

def soma(x ,y):
    return x + y  
soma1 = soma(3, 5)
soma2 = soma(4, 6)

print(soma1 + soma2)