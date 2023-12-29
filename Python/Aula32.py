"""
Flag (bandeira) - Marcar um local
None = Não valor
id e is not = é ou não (tipo, valor, identidade)
id = identidade
"""

condicao = False
passou_no_if = None

if condicao:
   passou_no_if = True
   print('Faça algo')
else:
    print('Não faça algo')

#print(passou_no_if, passou_no_if is None)
#só quando tem valor vaii dar True
#print(passou_no_if, passou_no_if is not None)
#só quando tem valor que vai dar True
    
if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou pelo if')
#aqui e para ele faz  averificação se passou ou não.
