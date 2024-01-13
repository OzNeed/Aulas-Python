"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Bruno', 'Bruna']
lista_b = lista_a.copy()#com o .copy(), faz com que crie uma nova lista. Não sendo o mesmo valor de memória.

lista_a[0] = 'Quaquer coisa'
print(lista_b)