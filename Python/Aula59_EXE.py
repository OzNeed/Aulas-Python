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
    botao_permitido = 'ial'

    if botao not in botao_permitido:
        os.system('cls')
        print('Digite uma das opções informadas!')
        continue
    
    if botao == 'i':
        inserir = input('Digite o que deseja inserir: ')
        lista.append(inserir)
        os.system('cls')
            
    if botao == 'a':
        apagar = input('Digite o indice que deseja apagar: ')
        if len(apagar) >= 2:
            os.system('cls')
        try:
            apagar = int(apagar)
            del lista[apagar]
            os.system('cls')
        except ValueError:
            print('Digite um número inteiro')
            os.system('cls')
        except IndexError:
            print('Digite um índice válido!')
            os.system('cls')
        except Exception:
            print('Erro desconhecido!')
            os.system('cls')
    # Except e a melhor forma tratar com o erro que pode dar para retorna a mensagem correspondente ao erro.
    if botao == 'l':
        os.system('cls')
        if 0 == len(lista):
                os.system('cls')
                print('Não há nenhum indice para mostrar!')
        for indice, nome in enumerate(lista):
            print(indice, nome)