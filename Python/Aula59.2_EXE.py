import os
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar listar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except TypeError:
            print('Digite um índice válido!')
        except Exception:
            print('Erro desconhecido!')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        for indice, nome in enumerate(lista):
            print(indice, nome)
    