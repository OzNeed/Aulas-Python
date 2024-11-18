# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis

# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
    ]
# print(lista)

# Mapeamento de dados em list comprehension
# Um mapeamento e fazer um para um, vendo que o valor da lista 1 e o mesmo na lista numero 2, só que houven modificação, como exemplo abaixo:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


produtos = [
    {'nome':'p1', 'preco': 20,},
    {'nome':'p2', 'preco': 10,},
    {'nome':'p3', 'preco': 30,},
]

novos_produtos = [{**produto, 'preco': produto ['preco']* 1.05} 
    if produto['preco'] > 20 else {**produto} 
    for produto in produtos
]
# print(novos_produtos)
# print(*novos_produtos, sep='\n')

lista = [n for n in range(10) if n < 5]
# print(lista)

novos_produtos = [{**produto, 'preco': produto ['preco']* 1.05} 
    if produto['preco'] > 20 else {**produto} 
    for produto in produtos
    if produto['preco'] > 10
]
print(*novos_produtos, sep='\n')

# Mapeamento e pegar um dado e jogar em outra lista, e ambas as lista tem o mesmo tamanho