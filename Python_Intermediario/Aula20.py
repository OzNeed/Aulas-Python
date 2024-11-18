# Sets - Conjuntos em Pyhton (tipo set)

# Conjuntossão ensinados na matemática
# brasilescola -> matematica -> conjunto
# Representandos graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém acetitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# ele só tem valor, não tem cheve e valor como dicionário

# Sets são eficientes para ermover valores duplicados de iteráveis
# - eles não tem índexes;
# - eles não garante ordem;
# - eles são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Métodos úteis:
# add, update, clear, discard
# add, só aceita um valor por vez

s1 = set()
s1.add('Bruno')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# Para passar outros valores tem que coloca dentro dentro de uma tupla, se não ele vai iterar
# s1.clear() limpar tudo
# s1.discard('Olá mundo') para descartar uma valor, basta inserir o nome do valor
print(s1)

# Operadores úteis
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

