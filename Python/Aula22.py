# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para respresentar um não valor

#entrada = input ('[E]Entrar [S]Sair')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'
# No python se colocar entre parentêses pode ser considerado
# uma expressão inteira, então ele vai avaliar antes
# dar continuidade no resto do processo. Caso seja verdadeira
#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#    print('Entrar')
#else:
#    print('Sair')

# valiação de curto circuito
print(True or False)
print ( 0 or False or 0 or "abc")

senha = input('Senha :') or 'Sem senha'
print(senha)