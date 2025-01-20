# dir, hasattr e getattr em Python
string = "Bruno"
metodo = 'lower'

# print(string)
# dir -> mostra todos os nome definidos dentro de string
# hasattr -> check se um determinado objeto tem determinado nome dentro
# Sempre que for validar o objeto tem que colocar ele como str, segue exemplo: hasattr(string, 'upper')

if hasattr(string, 'upper'):
    print("Existe upper")
    print(getattr(string, metodo)()) #Quando se trata de um imutavél, e bom sempre fazer dessa forma
else:
    print('Não exite o método', metodo)