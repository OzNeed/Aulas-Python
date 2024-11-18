# Sets são eficientes para ermover valores duplicados de iteráveis
# - eles não tem índexes;
# - eles não garante ordem;
# - eles são iteráveis (for, in, not in)

# l1 = [1,2,3,3,3,3,3,3,1,4]
# s1 = set(l1)
# l2 = list(s1)
#   s1 = {1,2,3,3,3,3,3,3,1,4}
# print(l1)
# print(s1)
# print(l2)

s1 = {1,2,3}
print (3 not in s1)
for numero in s1:
    print(numero)
# Toda vez que aparecer o erro "unhashable" e que se trata de um valor mutável dentro do set
# Problema e que o set não garante a ordem

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
