frase = 'O Python é uma linguagem de programação'\
    'Multiparadigma.'\
    'Python foi criado por Guido van Rossum.'
#Barra invertida e para quebrar a linha e continuar o código na linha de baixo.

#print(frase.count(""))

i = 0
qtd_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    
    Verificar = frase.count(letra_atual)

    if qtd_mais_vezes < Verificar:
        qtd_mais_vezes = Verificar
        letra_apareceu_mais_vezes = letra_atual

    i += 1
print(f'A letra que apareceu mais vezes foi: {letra_apareceu_mais_vezes}')
print(f'Que apareceu: {qtd_mais_vezes}')