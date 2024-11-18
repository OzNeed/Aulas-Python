# Sets - Conjuntos em Pyhton (tipo set)

# Conjuntossão ensinados na matemática
# brasilescola -> matematica -> conjunto
# Representandos graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém acetitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# ele só tem valor, não tem cheve e valor como dicionário

s1 = set() # Vazio
s1 = {'Bruno', 1,2,3} #com dados
# print(s1)

# Sets são eficientes para ermover valores duplicados de iteráveis
# - eles não tem índexes;
# - eles não garante ordem;
# - eles são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos