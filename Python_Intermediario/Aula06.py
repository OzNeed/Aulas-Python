"""
Retorno de valores das funções (return)
"""

# def soma(x, y):
#     # Somente a função e métodos tem o return
#     return x + y 
# Essa função retorna o valor, e pode mandar para qualquer lugar que quiser.
    # Após colocar o return o Python entende que tem parar tudo o que está fazendo e se colocar novas funções pós, não vai funcionar, mas antes dela pode ter outras coisas.
# variavel = soma(1, 2)
# variavel = int('1') # Essa e uma função que retorna um valor.

def soma (x, y):
    if x > 10:
        return "Pode está colocando qualquer valor"
    return x + y
# No caso acima se trata de um retorno em uma condição de verdadeiro ou falso, podendo colocar esses validadores para colocar mais de um return. mas nesse exemplo do 10, 20, isso e uma tupla e ele retorna os valores e não soma.

soma1 = soma(2, 2) # Nessa função tem que pegar o valor de dentro dela para está fazendo outras atividades com o valor da várivel.
soma2 = soma(3, 3)
# Nessa função tem que pegar o valor de dentro dela para está fazendo outras atividades com o valor da várivel.
# Agora com a função return, o valor vai para a várivel e reflete em outras ações
print(soma1)
print(soma2)
print(soma(20,33))