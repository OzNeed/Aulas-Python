# Desempacotamento em chamadas
#  de métodos e funções

salas = [
    #   0         1
    ['maria', 'Helena'], #0
    #   0
    ['Elaine'], #1
    #   0       1        2
    ['Luiz', 'João', 'Eduarda',] #(0, 10, 20, 30, 40)]#2
]

# string = ['ABCD']
# lista = ['Maria', 'Helena', 1, 2, 3, 'Eduardo']
# tupla = 'Python', 'é', 'legal'

# # a, b, *_, ap, c = lista
# # print(a, ap)

# # for nome in lista:
# #     print(nome, end=' ')
# print(*lista)
# print(lista)
# print(*tupla)

print(*salas, sep='\n')
# end='' Seria para colocar um função no final da linha
# sep='' Para separar no espaços entre cada valor