"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 #Velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

#Sempre tentar minimizar a linhas de códigos, sempre posicionando
#algumas váriaveis em algum campo a parte só para ela.
#com isso tranforma o código muito mais limpo.
#como no exemplo abaixo, poderiamos, fazer uma várivel,
# para seber se o carrou passou ou não pelo radar.

vel_carro_passou_radar = velocidade > RADAR_1
Range_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE)
multa =  vel_carro_passou_radar and Range_radar

if vel_carro_passou_radar:
    print("Carro está acima da velocidade")

if Range_radar:
    print("Carrou passou pelo radar!")

if multa:
    print("Carro foi multado!")