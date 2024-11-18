def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def criar_multiplicado(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# duplica = criar_multiplicado(2)
duplica = executa(
    lambda m: lambda n: n*m,
    2
)
print(duplica(2))

print(
    executa(
        # e a mesma coisa que fazer o def soma
        lambda x, y: x + y,
        2, 3
    )
)

print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7
    )
)