"""
Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - cocatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""

lista= [10, 20, 30, 40]
lista.append('Bruno')
#nome = lista.pop()
del lista[-1]#último da lista
#lista.clear()
lista.insert(0, 5)#primeiro número seria o indice, o segundo e o valor que deseja.
#Se colocar um indice que não existe como 100, pode até colocar. Mas ele não vai ficar com esse indice, mas sim com o último que seria o 5.
print(lista)
