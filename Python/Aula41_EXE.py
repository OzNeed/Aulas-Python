""" Calculadora com while

sair = sair.lower() #Esse metódo transforma toda letra maiuscúla em minuscúla. também reaproveitando a variável de cima.

sair = sair.startswith('s')#o startswith e para ver a primeira letra que foi inserida no input.
"""
while True:
    numero_1 = input('Digite um número: ')
    operador = input('Digite o opeador (+-/*): ')
    numero_2 = input('Digite outro número: ')

    numeros_validados = None # uma flag para validar
    num_1_float = 0
    num_2_float = 0
    try:
        #conversor para validar o número.
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validados = True

    except:
        
        numeros_validados = None

    if numeros_validados is None:
        print('Um ou ambos os número digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'
    #validar se o operador que informou e o correto.
    if operador not in operadores_permitidos:
        print('operador inválido.')
        continue
    #validar se o usuário digitou mais de um número.
    if len (operador) > 1:
        print('Digite apenas um operador.')
        continue
    # o código acima e um validados, onde sempre e bom validar o que o usuário está digitando.
    if operador == '+':
        print(f'A soma dos valores é: {num_1_float + num_2_float}')
    
    elif operador == '-':
        print(f'A subtração dos valores é: {num_1_float - num_2_float}')

    elif operador == '*':
        print(f'A multiplicação dos valores é: {num_1_float ** num_2_float}')

    elif operador == '/':
        print(f'A divisão dos valores é: {num_1_float / num_2_float}')

    sair = input('Deseja sair? [s]im ou [n]ão: ').lower().startswith('s')
        
    if sair is True:
        print('Desligando!')
        break
    else:
        continue    