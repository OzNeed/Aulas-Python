"""while/else"""

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break

    print(letra)
    i += 1
else: # se inserir um break dentro do while, o else não irá se utilizada.
    print('Não encontrei um espaço na string')
print('Fora do código')