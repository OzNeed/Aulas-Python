# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# retorne o total para uma variável e mostre o valor 
# da variável.

# crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
numero = []

def mult(*args):
    resultado = 1
    for num in args:
        resultado *= num
        
    def div():
        return resultado % 2 == 0
    
    is_divisivel = div()
    print("*"*30)
    print(f'O resultado da multiplicação: {resultado}')
    if is_divisivel:
        print("valor é divisivel!")
        print("*"*30)
    else:
        print("O valor não é divisivel!")
        print("*"*30)
    return resultado

while True:

    print("Adicione [a] calcular [c] sair [s]")
    letra = input("Digite uma opção: ")

    if letra == 'a':
        valor = input("Digite um numero: ")
        numero.append(int(valor))
        continue
    elif letra == 'c':
        valor = tuple(numero)    
        result_multiplicar = mult(*valor)
        print("Resultado impresso acima!")
        break
    elif letra == 's':
        print("Programa fechado!")
        break
    else:
        print("Digite um valor válido!")
        continue