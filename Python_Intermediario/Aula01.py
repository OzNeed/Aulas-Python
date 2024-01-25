"""
Introdução às funções (def) em Python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""
# o Print tem parametros que em determinado momento vai receber algum argumento

def Print(a, b, c):
    print ('Várias1')
    print ('Várias2')
    print ('Várias3')
    print ('Várias4')
print('')
print('')
#quando se referir ao parâmetro, está falando o que vai dentro do parentese no def.
def imprimir(a, b, c):
    print(a, b, c)

# #quando está se referindo ao valor, e o valor que e passado dentro do parentese pedindo para executar.
imprimir(1, 2, 3)
imprimir(4, 5, 6)
#caso o valor seja definido dentro do def, ai vai mostrar o que foi alimento dentro do executor.
#pode ser alterado quando quiser os parâmetros, quando for chamado ele
print('')
print('')
#pode também definir um valor dentro do def, para não ter erro ao chamar ele
#pois ele e como se fosse uma váriavel
def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Bruno Alves')
saudacao('Bruno')
saudacao('Bruna')
saudacao()