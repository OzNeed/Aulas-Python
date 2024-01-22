"""
calculo do primeiro digito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos calores por uma
contagem regressiva começando de 10

ex.: 746.824.890-70(749824890)
    10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

    Somar todos os resultados:
    70+36+48+56+12+20+32+27+0 = 301
    Multiplicar o resaultado anterior por 10
    301 * 10 = 3010
    Obter o resto da divisão da conta anterior por 11
    3010 % 11 = 7
    Se o resultado anterior for maior que 9:
        resultado é 0
    contrário disso:
        resultado é o valor da conta

O primeiro dígit do CPF é 7
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
        print(f'O valor é: 0' if resto > 9 else 'O digito é: ', resto)
        continue

    else:
        os.system('cls')
        print('Digite um CPF válido, verifique e corriga os dados!')