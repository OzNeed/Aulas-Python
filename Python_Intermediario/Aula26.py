# Empacotamento e desempacotamento de dicionário

a, b = 1, 2
a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)


# for chave, valor in pessoa.items():
#     print(chave, valor)

# args e kwargs
# args (já vimos)
# kwargs - Keyword arguments (argumento nomeadodos)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idaide': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)


    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'args1': 1,
    'args2': 2,
    'args3': 3,
    }

mostro_argumentos_nomeados(**configuracoes)