"""
args - Argumento não nomeados
* - *args (empaxotmaneto e desempacotamento)
"""
# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

# elementos não nomeados
def soma(*args):

    # acumulador
    total = 0
    for numero in args:
        print("Total", total, numero)
        total += numero
        print(total)

soma(1, 2, 3, 4, 5, 6)