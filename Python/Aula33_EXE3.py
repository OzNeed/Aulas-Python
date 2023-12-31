"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 letras "Seu nome é muito grande".
"""

nome = input('Digite o seu meu primeiro nome:')
conve = len(nome)

if conve > 1:
    if conve <= 4:
        print('Seu nome é curto')
    elif conve >= 5 and conve <= 6:
        print('Seu nome é normal')
    else :
        print('Seu nome é muito grande')
else:
    print('Não digiotu nada!')