lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))
# Sempre o valor do lado esquerdo do for na list compreehesion e o valor que vai ser incluido.
# Para inclui mais de um for dentro, basta manipular e inserir como tupla o valor a esquerda
# lista = [
#     (x, y)
#     for x in range(3)
#     for y in range(3)
# ]

lista = [
    [(x, letra) for letra in "Bruno"]
    for x in range(3)
]

print(lista)

