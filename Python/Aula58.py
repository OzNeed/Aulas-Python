"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
#Ele inumera os itens da lista.
#lista_enumerada = list(enumerate(lista, start=22))
#'start=' informa de onde queira começar.
#print(lista_enumerada)

#for item in enumerate(lista):
#   indice, nome = item
#   print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
# Fazendo isso, faz com que ele desempacote ele da tupla, gerando um for dentro de outro for.
# Pois ele vai separando o indice e nome, acada volta que faz.
# Utilizando direto no for, pode utilizar quantas vezes quiser. Pois se fizer com uma váriavel ele vai consumir todos os dados e após não vai ser possivel utilizar mais.
    
#for tupla_enumerada in enumerate(lista):
#    print('FOR da tupla:')
#    for valor in tupla_enumerada:
#        print(f'\t{valor}')
        #isso e para dar equivalente a 4 espaços, como o tab e feito. o \n para quebrar linha