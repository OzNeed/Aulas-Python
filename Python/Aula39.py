"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    #enquanto o primeiro while roda uma vez, o segundo vai rodar 5 vezes. Pois até completar as colunas para começar uma nova linha.
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')#Colocar o = após a variável vai mostrar o nome da variável e o número.
        coluna +=1
    linha += 1

print('Acabou')