"""
Execício
Peça ao usuário para digitar seu nome
Peça ao usuário para diogitar sua idade
Se nome e iade forem digitadas:
    Exiba:
        Seu nome é{nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaço
        Seu nome tem {n} letras
        A primeira leta ddo seu nome é {letra}
        A última letra o seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome:')
idade = input('Digite a sua idade:')

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome [::-1]}")
    if " " or nome:
        print("Nome contém espaço")
    else:
        print("Nome não contém espaço")
    print(f"Primeira letra do nome: {nome[0]}")
    print(f"A última letra do nome é: {nome[-1]}")
    
    

else:
    print("Desculpe, você deixou campos vazios.")