# operadores in e not in
# String são iteráveis
# 0 1 2 3 4, sempre comçar do zero no positivo
# B r u n o
# -5-4-3-2-1, sempre colocar do -1 vindo no negativo

#nome = "Bruno"
# print(nome[3])
# print(nome[-2])

#print('no' in nome)
#print("Br" in nome)
#print(10*'-')
#print('nO' not in nome) # Como ele está no nome ai ele vai dar falso, caso não esteja na palavra vai dar True
#print("br" not in nome) # Pois o not in ele vai validar se não está, mas como está por isso e True

nome = input("Difite o seu nome:")
encontrar = input ("Digite o que deseja encontrar:")

if encontrar in nome :
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')