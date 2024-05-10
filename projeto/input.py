nome = input ('Qual o seu nome? ') #só ler strings
print (f'Seu nome é {nome}')
#numero= int(input ('Digite um numero:'))#converte em int, mas erra se por algo diferente
numero_1 = input('Digite um numero: ')
numero_2 = input('Digite mais um numero: ')
int_numero1 = int(numero_1)#Para converter em int, mas ainda pode dar erro
int_numero2 = int(numero_2)#Precisa de um condicional pra resolver
print (int_numero1 + int_numero2)