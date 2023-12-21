# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(1+3.5) #soma de dois número, pois passa dois tipo
#print('1'+1) #aqui o interpretador não consegue concatenar os dois
print('a'+'b')

print(int('1'), type(int('1')))
print(int('1')+1)#nesse caso, estamos convertendo a str em um int, pois usamos a classe "int()" para fazer a conversão. Isso funciona para os demais também como float, bool, string.
print(type(float('1')+1))#ele vai executando dos parenteses de dentro para fora, como na sequencia float, após vai realizar a soma, após ver o tipo e por fim vai imprimir o valor.
print(bool(' '))#classe vazia e consederado False e com um valor e True.
print(str(11)+'b')#conversão de números para str
