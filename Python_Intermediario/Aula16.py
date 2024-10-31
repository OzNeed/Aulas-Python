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

p1 = {
    'nome': 'Bruno',
    'sobrenome': 'Alves',
}

# print(p1.get('nome1', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# remove a última chave do dicionario
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)   

# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = ('nome', 'novo valor'),('idade', 30)
lista = [['nome', 'novo valor'],['idade', 30]]
p1.update(lista)
print(p1)