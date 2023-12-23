"""
Fatiamento de string

012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::] [inicio:fim:passo]
Obs.: A função len retorna a qtd de caracteres da str

"""

variavel = 'Olá mundo'
print(variavel[-8:-2]) #Sempre colocar um número acima do indice que deseja.
print(len(variavel)) #Serve para contar quantos idice tem a variavel ou frase que deseja

print(variavel[0:9:1])
print(variavel[0:9:2])#pula e pega a próxima letra
print(variavel[0:9:3])#pula duas e pega a próxima letra
print(variavel[0:9:4])#pula trê e pega a próxima letra

print(variavel[::-1])#vai inverte a string
print(variavel[-1:-10:-1])
print(variavel[-1:-10:-2]) # começa de trás para frente