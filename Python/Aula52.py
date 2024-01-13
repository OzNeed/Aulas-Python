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

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
# Esse metódo não retorna nada, não retorna nenhum valor. Mas altera direto na variavel informada.
print(lista_a)
print(lista_b)
print(lista_c)
print(lista_d)
