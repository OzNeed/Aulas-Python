"""
Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""

lista =[10, 20, 30, 40]
#lista[2] = 300
#del lista[2] #Quando deleta algum indice na lista ele move os outros indices para reogarnizar os indices
#print(lista)
#print(lista[2])
lista.append(50)#para adicionar valores ao final da lista, com isso vai somar mais um indice na lista.
lista.pop()#vai apagar o último elemento antes dela ser executada
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)