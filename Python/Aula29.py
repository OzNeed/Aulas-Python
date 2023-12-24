"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

print(1234)
print(5678)

#float('a')

numero_str = input('Vou dobrar o número que você digitar:')

try:   
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro do número {numero_str} é:  {numero_float*2:.2f}')
except:
    print('Isso não e um número')

#if numero_str.isdigit():
#    numero_inteiro = int(numero_str)
#    print(f'O dobro do número {numero_str} é:{numero_inteiro*2}')
#else:
#    print('Isso não e um número')