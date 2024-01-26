"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y,z):
    #Definição
    print(f'{x=} y={y} {z=}', '|','x+y+z=', x + y + z)
    #para verificar se o parametro e igual ao valor, tem dois jeitos que foram feito acima
soma(1, 2, 3)#argumentos posicionais 
soma(y=2,z=3, x=1)#argumentos nomeados
soma(1, y=2, z=5)
#Se nomer um parametro, os outros valores que vierem após. Deve ser nomeado, se não irá ter um erro
print(1, 2, 3, sep='-')

soma#nome da função
