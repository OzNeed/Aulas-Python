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

# Operadores úteis
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 # juntar os dois set e remover os duplicados
s4 = s1 & s2 # Mostra quais valores estão presentes em ambos set
s5 = s1 - s2 # mostra o valor exclusivo no set da esquerda
s6 = s1 ^ s2 # Mostra os valores presentes que são exclusivos do set
print(s3)
print(s4)
print(s5)
print(s6)