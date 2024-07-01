"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)
# o que está em parênteses vai funcionar da seguinte maneira, primeiro vai receber o valor da funcao que está na função e posterior o valor que vai executar outra função para retorna o "bom dia"
print (executa(saudacao, "Bom dia", "Bruno"))
print (executa(saudacao, "Bom dia", "Luiz"))
