"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra global faz uam variável do escopo externo
ser a mesm no escopo interno.
"""

x = 1

#Seria a mesma coisa de definir uma váriavel
def escopo ():
    # global x é má prática informa isso dentro da váriavel
    x = 10
#Váiaveis de escopo interno pode atingir as váriaveis de escopo externo, mas de escopo externo não pode atigir a de interno.
    def outro_escopo():
        # global x
        x = 11
        y = 2
        print(x, y)
    
    outro_escopo()
    print(x)

print(x)
escopo()
print(x)