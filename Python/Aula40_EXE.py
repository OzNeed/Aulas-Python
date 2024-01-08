"""
Interando strings com while
"""
#       012345678910
#nome = 'Bruno Alves' #interáveis
#       -11

#tamanho_nome = len(nome)
#print(nome)
#print(tamanho_nome)
#print(nome[0])

nome = 'Bruno Alves'

indice = 0 # invés de pedir convencional da forma : nome[0], pode infoma desse jeito como indice = 0
novo_nome = ''
while indice < len (nome):
    letra= nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome +='*'
print(novo_nome)