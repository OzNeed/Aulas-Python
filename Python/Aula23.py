# Operador lógico "not"
# Usado para inverter expressões
# not True = False
#not False = True

senha = input('Senha:')

if senha == '123456':
    print("entrou")
else:
    print("Digitou errado")

if not senha:#invés de fazer o comparativo se digitou certo, ele irá agir como se fosse um else dando como "False"
    print("Digitou nada")
else:
    print("você entrou")

print (not True) #False
#ele inverte a expressão verdadeiro para falso
print(not 0) #True
#ele inverte a expressão false para verdadeiro