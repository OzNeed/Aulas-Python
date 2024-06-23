"""
args - Argumento não nomeados
* - *args (empaxotmaneto e desempacotamento)
"""
# Lembre-te de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

# elementos não nomeados
# utilizado para passar caracteres ilimitados não nomeados
def soma(*args):

    # acumulador
    total = 0
    for numero in args:
        total += numero
    return total

# soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

numeros = 4, 5, 6
soma_4_5_6 = soma(*numeros)
print(soma_4_5_6)

# # O "*" serve para está espalhando o números e retirar da tupla que vem por padrão
# # print(*numeros)
# print(sum(numeros))