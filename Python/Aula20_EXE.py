primeiro_valor = input('Dgite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f"Primeiro valor {primeiro_valor} e maior que o segundo valor {segundo_valor}")
elif segundo_valor>primeiro_valor:
    print(f"O segundo valor {segundo_valor} e maior que o primeiro valor {primeiro_valor} ")
else:
    print("Os valores são iguais")
