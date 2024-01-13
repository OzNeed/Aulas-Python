"""
Exercício
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Bruno')

i = 0
while i < len(lista):
    indices = i
    print(f'o indice é: {indices}')
    nome_lista = lista[i]
    print(f'O nome é: {nome_lista}')
    i += 1 

print(' ')
print('Acabou o meu código, agora o código do curso abaixo:')
print(' ')

#Resolvido no curso!

lista_1 = ['Maria', 'Helena', 'Luiz']
lista_1.append('Bruno')

indices = range(len(lista_1))

for indice in indices:
    print(indice, lista_1[indice], type(lista[indice]))