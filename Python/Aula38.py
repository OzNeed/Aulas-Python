"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

break -> O código vai para idependete quando ler esse código. Pois ele deve ser após do Print, para não quebrar no meio a função.
"""

contador = 0

while contador <= 100:
    contador += 1 # Isso que controla o contador

    #Se coloca algum if com o valor que deseja pular ele vai fazer o oposto
    if contador == 6:
        print('Não vou mostrar o 6!')
        continue
    #O termo (continue) serve para pular um determinado valor, como informado acima que foi o 6 e abaixo que foi entre o 10 até o 27.
    if contador >= 10 and contador <= 27:
        continue
    
    print(contador)
    
    if contador == 40:
        break

print('Seria o oposto que é, invés de omitir vai só informa o que deseja pular')

#while contador <= 100:
#    if contador == 6:
#        print('Não vou mostrar o 6!')
#        continue
#
#    contador += 1
#    #Se coloca algum if com o valor que deseja pular #ele vai fazer o oposto
    
    #O termo (continue) serve para pular um determinado valor, como informado acima que foi o 6 e abaixo que foi entre o 10 até o 27.
#    if contador >= 10 and contador <= 27:
#       continue    

#print (contador)

#    if contador == 40:
#        break