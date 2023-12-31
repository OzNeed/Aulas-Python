"""
Faça um program que pergunte a hoa ao usuáio e, baseando-se no horário
descrito, exiba a sauadção aprorpiada. EX.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#Meu código!
#bom_dia = 23 - 12
#boa_tarde = 23 - 6
#boa_noite = 23

#hora = int(input('Digite a horá:'))

#if hora <= bom_dia:
#    print('Bom dia, tenha um ótimo dia!')
#elif hora <=boa_tarde:
#    print('Boa tarde, tenha uma tarde maravilhosa!')
#elif hora <= boa_noite :
#    print('Boa noite, desejo um bom descanso!')
#else:
#    print('Não digitou nada!')

#Código da aula

entrada = input('Digite a hoa em números inteiros:')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia, tenha um ótimo dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde, tenha uma tarde maravilhosa!')
    elif hora >=18 and hora <=23:
        print('Boa noite, desejo um bom descanso!')
    else:
        print('Não conheço esse hora!')
except:
    print('Por favor, digite um números inteiros!')