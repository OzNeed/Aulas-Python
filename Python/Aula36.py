"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador < 10:
    contador = contador + 1#ele vai somar mais um na próxima vez que o while passar, pois ele sempre vai pegar o antigo valor e soma por 1.
    print(contador)

print('Próximo, que vai começar imprimindo o 0 e não o número 1')

while contador <= 10: # Ele vai começar com o 0, mas o número 10 ele não e equivalente ao valor (10), mas para começar a imprimir o valor 10 tem que inserir o = para fazer essa verificação.
    print(contador)
    contador = contador + 1