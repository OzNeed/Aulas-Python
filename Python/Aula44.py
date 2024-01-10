#texto = 'Python'

#i = 0
#tamanho_string = len(texto)
#while i < tamanho_string:
#    print(texto[i], i)
    
#    i += 1
texto = 'Python'
novo_texto = ''
# A 'letra' pode colocar qualquer coisa pois, o for vai colocar todos os elementos do 'texto'.
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')

# Teste rápido!
#print ('Acabou a primeira fase!')

#texto_new = 'Olá pessoal'

#o = 0
#tamanho_texto = len(texto_new)
#while o < tamanho_texto:
#    print(texto_new[o])

#    o += 1