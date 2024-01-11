"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entegue seu iterador
"""
#Toda vez que for utilizar o "for", ele vai pedir o elemento __iter__ dos
#numeros = range(0, 100, 8)

#for numero in numeros:
#    print(numero)

#esse metodo e a mesma que __iter__
#texto = iter('Bruno')
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#Ele vai mostrar cada letra uma por vez, sempre mostrando o próximo valor
#print(next(texto))
#print(next(texto))
#print(next(texto))
#print(next(texto))
#print(next(texto))
#Tem esses dois modulos de se utilizar o next() ou .__next__

# for letra in texto
texto = 'Bruno' # iterável
iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
print(' ')
print('Outra forma abaixo:')
print(' ')
#se for feito com o for vai ficar desse jeito.
texto_new = 'Among' # iterável

for letra in texto_new:
    print(letra)