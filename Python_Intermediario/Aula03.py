"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será 
usado.
Refatorar: editar o seu código.  
"""

#todo valor que vier com valor padrão, os que vão vim após vão ter que está com valor padrão
#como a segui, o z=None, então o valor que vier após isso também tem que vir com valor padrão.
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
#para mostrar uma variável que recebe o valor como None, pode inserir um validador para verificar. Com o "is not".
#pois ai vai mostra o valor que não for None.