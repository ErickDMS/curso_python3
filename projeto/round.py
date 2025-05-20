import decimal


numero1 = decimal.Decimal(0.1) ##mais usado para pontos flutuantes muito grandes
numero2 = decimal.Decimal(0.7)

numero3 = numero1 + numero2
print(numero3)
print(round(numero3, 2))