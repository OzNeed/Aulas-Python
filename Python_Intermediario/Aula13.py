# Dicionarios em Python (tipo dict)
# Dicionario sao estruturas de dados do tipo par de "chave" e "valor"
# Chaves podem ser consideradas como o "indice"
# que vimos na lista e podem ser tipos imutaveis 
# como: str, int, flot, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro dicionario
# Usamos chaves {} ou a classe dict para criar dicionarios
# Imutaveis: str, int, float, bool e tuple
# Mutaveis: dict e list

# pessoa = {
#  "nome": "Bruno",
#  "sobrenome": "Alves",
#  "idade": 23,
#  "altura": 1.90,
#  "endereco":[
#    {"rua": "anun preto", "numero": 14},
#    {"rua": "Andorinha pequena", "numero": 285}
#  ]
#}

# print (pessoa["endereco"][1])
# print(pessoa, type(pessoa))

# for chave in pessoa:
  #print(chave, pessoa[chave])

# Aula de manipulacao de dicionarios

pessoa = {}
chave = 'nome'
pessoa[chave] = "Bruno"
pessoa["sobrenome"] = "Alves"

print(pessoa[chave])

pessoa[chave] = "Maria"
del pessoa["sobrenome"]
print(pessoa)
print (pessoa["nome"])

#print pessoa.get("sobrenome")
if pessoa.get("sobrenome") is None:
  print("Nao existe")
else:
  primt(pessoa["sobrenome"])