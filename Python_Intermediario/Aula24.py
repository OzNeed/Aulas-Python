# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única expressão.

# lista = [
#     {'nome': 'Bruno', 'sobrenome': 'Alves'}
#     {'nome':'Luiz','sobrenome':'mirando'}
#     {'nome':'Maria','sobrenome':'Silva'}
#     {'nome':'Daniel','sobrenome':'Silva'}
#     {'nome':'Eduardo','sobrenome':'Moreira'}
# ]

# lista = [4,32,1,34,5,6,6,21,]
# lista.sort(reverse=True)
# reverse=True, começar e trás para frente
# sorted(lista) Outra forma, mas cria uma lista rasa
lista = [
    {'nome': 'Bruno', 'sobrenome': 'Alves'},
    {'nome':'Luiz','sobrenome':'mirando'},
    {'nome':'Maria','sobrenome':'Silva'},
    {'nome':'Daniel','sobrenome':'Silva'},
    {'nome':'Eduardo','sobrenome':'Moreira'},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

# for item in lista:
#     print(item)

exibir(l1)
exibir(l2)