# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para respresentar um não valor

entrada = input ('[E]Entrar [S]Sair')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if True:
# Ele só vai dar continuidade a validação se todas as 
# validações for verdadeira.
# caso seja falsa ele não validar o resto.
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#Avaliação de curto circuito
# ele para no false pois para na expressão falsa 
# para de validar, pois o resto vai se validado como falso
print( True and False and True)
print(True and 0 and True)