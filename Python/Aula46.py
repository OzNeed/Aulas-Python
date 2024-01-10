"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entegue seu iterador
"""
#Toda vez que for utilizar o "for", ele vai pedir o elemento __iter__ dos
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)