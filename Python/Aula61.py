"""
split e join com list e str
split -divide uma string (retorna, list)
join - une uma string
"""
frase = '   Olha só que  ,   coisa interessante         '
lista_frases_cruas = frase.split(', ')
#se usar dessa maneira .split() sem informa nenhum dado para quebrar, ele vai quebrar nos espaços.  

lista_frases = []
# Fazendo dessa maneira, faz com que o .append, acrescente o indice da lista já corrigido na nova lista.
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
#strip() retira o espaço do inicio e fim
#rstrip() retira o espaço da direita
#lstrip() retira o espaço da esquerda

print(lista_frases_cruas)
print(lista_frases)

print('outro metódo de str!')
#só iteráveis que pode ser usados com o .join
frases_unidas = ', '.join(lista_frases)
# o separador das palavras vai está na aspas antes do .join, como no exemplo acima ''.join('abc'). Desse jeito vai resultar no abc como informado, mas se passar um valor '-'.join('abc'), vaui resultar em a-b-c.
print(frases_unidas)