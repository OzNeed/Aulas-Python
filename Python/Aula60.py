"""
Imprecisão de ponto flutuante
Double-precision floationg-point format IEEE 754
"""
import decimal
#Para utilizar esse módulo seria para realizar constas precisas, pois ele recebe o valor como uma str. Com isso ele faz a convesão de forma automática.
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')#Retorna como str
print(round(numero_3, 2))# Uma função para fazer como a opção acima. Retorna como float.

"""
Essas são as três forma de corrigir a impressição do cálculo do float.
"""
