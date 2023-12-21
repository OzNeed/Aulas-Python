"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
x - gera um Hexadecimal minuscúlo
X - gera um Hexadecimal maiuscúlo
"""

nome = 'Bruno'
preco = 1000.958789
# para chamar outras variavel dentro de outra, basta utilizar o "%", mas tem as regras para ser utilizada
#como vamos chamar o nome que e "%s", que é uma string
#e também o preco que "%f", que seria um número com ponto flutuante
variavel = '%s, o preço é R$%.2f' %(nome, preco) # só é colocado entre parenteses caso tenha mais de um valor
print (variavel)

print('o Hexadecimal de %d é %08X' %(1500,1500))
