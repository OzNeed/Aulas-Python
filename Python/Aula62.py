"""
Lista de listas e seus índices
"""
salas = [
    #   0         1
    ['maria', 'Helena'], #0
    #   0
    ['Elaine'], #1
    #   0       1        2
    ['Luiz', 'João', 'Eduarda',] #(0, 10, 20, 30, 40)]#2
]
#primeiro indice busca o indice da lista
#o próximo indice busca o valor dentro da lista que indicou o indice
#print(salas[1][0])
#print(salas[0][1])
#print(salas[2][2])
#print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)