"""
calculo do primeiro digito do CPF
CPF: 749.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos calores por uma
contagem regressiva começando de 10

ex.: 749.824.890-70(749824890)
    10  9  8  7  6  5  4  3  2
*   7   4  9  8  2  4  8  9  0
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
        rsultado é o valor da conta

O primeiro dígit do CPF é 7
"""
lista = []

while True:
    print('\nAo digitar o CPF, retire os pontos e vírgulas')
    digite_cpf = input('Digite o CPF que deseja verificar: ')    
    
    if len(digite_cpf) > 11:
        print('CPF possuí apenas 11 digitos!')
   
    add = []
    multiplicando = 10

    i = 0    
    while i <= 9:
        cpf_digitos = digite_cpf[:9]
        valor = i

        if multiplicando >= 2:
            resultado_1 = i * multiplicando
            i += 1
            multiplicando = multiplicando - 1
            resultado_1 = resultado_1
            add.append(resultado_1)
        print(add, end=' '"\n")


                