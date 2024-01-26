"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
#escopo do arquivo
x = 1#escopo global

#Se for atribuido antes de definir a função ao vai ser válido, mas se for após pode.
def escopo():
    global x #para mexer na variavel de fora. pois ele puxa a última vez que mexe na variavel do mesmo nome
    x = 10#escopo local, pois ela e protegida pela função
    def outra_funcao():
        #só vai ter acesso ao x do escopo, pois e vizinho. Mas se fosse o contrario não era permitido
        x = 11
        y = 2 # esse y só pode ser utilizado na (outra_funcao)
        print(x, y)
#pode acessar variaveis dos escopos fora, mas não interno
    outra_funcao()
    print(x)

# x =1 # Dessa maneira também e permitido
print(x)
escopo()
print(x)#esse x vai ser igual ao de dentro da função, pois foi após a execução do def
