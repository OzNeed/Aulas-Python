# Metodos úteis dos dicionarios em Python
# len - Quantas chaves
# keys - iterável com chaves
# values - iterável com valores
# items - iterável com chaves e valores
# setdefault - Adiciona uma chave com um valor
# copy - retorna uma copia rasa (shallow copy)
# get - obtem chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro
# clear - apaga todos os itens

pessoa = {"Nome": "Bruno", "sobrenome": "Alves"}

print(len(pessoa)) # quantas chaves tem
print(pessoa.keys()) # todas as chaves e valores
print(list(pessoa.values())) # Mostra só os valores
print(list(pessoa)) # mostra todas as chaves e valores por indices
pessoa.setdefault("idade", "22")
# print(pessoa("idade"))