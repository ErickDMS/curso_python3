a = 'A'
b = 'B'
c = 1.1
string = 'a={0} b={1} c={2}'
string2 = 'a={1} b={2} c={0}'
string3 = 'a={2} b={0} c={2}'
string4 = 'a={nome1} b={nome2} c={nome3}'
formato = string.format(a, b, c)
formato2 = string2.format(a, b, c)
formato3 = string3.format(a, b, c)
formato4 = string4.format(nome1= a, nome2= b, nome3= c)
print (formato)
print (formato2)
print (formato3)
print (formato4)