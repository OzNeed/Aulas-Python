"""
Introdução ao desempacotamento + tumple (tuplas)
Pode fazer com qual valor iterável.
"""
#nomes = ['Maria', 'Helena', 'Luiz']
_,_, nome3, *_ = ['Maria', 'Helena', 'Luiz']
# Para empacotar os restos dos valores, deve ser inserido o '*' antes do nome, para empacotar os restos dos valores.
#Desenvolvedor usa o '_' para empacotar o resto
print(nome3)