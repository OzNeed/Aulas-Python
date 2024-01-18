"""
Coleta os 9 digitos do CPF
multiplar o valor começando por 10

após isso somar todos os valores
multiplicar a soma por 10
obter o resto da divissão da conta anterior por 11%

se o resultado anterior for maior que 9, o resultado e 0
contrário disso e o resultado do valor
"""
import os

multiplicador = 10
add = []
mult = []
i = 0
m = 0
s = 0

while True:
    print('\nDigite o CPF sem "." e "-".')
    cpf_digitado = input('Digite o CPF:')
    cpf_digitos = (cpf_digitado [:9])
    
    if len(cpf_digitado) <= 11:
                
        for adicionar in cpf_digitos:
            validador = cpf_digitos[i]
            add.append(validador)
            i += 1

        for multiplicar in add:
            if len(add) <= len(cpf_digitado):
                multiplicar = int(add[m])
                mult.append(multiplicar * multiplicador)
                multiplicador -= 1
                m += 1
        soma = sum(mult)
        multi = soma * 10
        resto = multi % 11

        os.system('cls')
        print('lista dos indices do CPF:', end=' ')
        print(add)
        print('\nLista dos indices multiplicados:', end=' ')
        print(mult)
        print('\nSoma de todos os valores:', end=' ')
        print(soma)
        print('\nO resto, que será o primeiro digito:', end=' ')
        print(resto)

    else:
        os.system('cls')
        print('Digite um CPF válido, verifique e corriga os dados!')
        


