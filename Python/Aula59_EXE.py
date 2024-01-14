"""
Faça uma lista de comprar com listas
O usuário deve ter a possibiliade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os

lista = []
while True:
    print('Selecione uma opção abaixo')
    botao = input('[i]nserir [a]pagar [l]istar: ')
    
    if botao == 'i':
        inserir = input('Digite o que deseja inserir: ')
        lista.append(inserir)
        os.system('cls')
        continue
            
    if botao == 'a':
        apagar = input('Digite o indice que deseja apagar: ')
        if len(apagar) >= 2:
            os.system('cls')
            continue
        else:
            apagar = int(apagar)
            lista.pop(apagar)
            os.system('cls')
            continue
    
    if botao == 'l':
        if 0 == len(lista):
                os.system('cls')
                print('Não há nenhum indice para mostrar!')
                continue
        for indice, nome in enumerate(lista):
            print(indice, nome)
            continue