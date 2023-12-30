"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuáio não digite um númeo inteiro,
informe que não é um número inteiro.
"""
num = input('Digite um número:')
try:
    inteiro = int(num)
    if "." or inteiro:
        print('Número inteiro')
        if (inteiro % 2 == 0):
            print('O número e par')
        else:
            print('O número e ímpar')
except:
    print('O número digitado é um float')

