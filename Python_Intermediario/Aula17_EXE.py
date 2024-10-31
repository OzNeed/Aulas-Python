# Exercício - sistema de perguntas e respostas

perguntas = [
    {
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4',
    },
    {
    'Pergunta':'Quanto é 5*5?',
    'Opções':['25', '55', '10', '51'],
    'Resposta':'25',
    },
    {
    'Pergunta':'Quanto é 10/2?',
    'Opções':['4', '5', '2', '1'],
    'Resposta':'5',
    },
]

erro = 0
acerto = 0

for pergunta in perguntas:
    print(pergunta.get("Pergunta", []))
    print("Opções:")


    opcoes = pergunta["Opções"]
    for opcao, valor in enumerate(opcoes):
        print (opcao, valor)


    escolha = input("Selecione a resposta: ")

    acertou = None
    escolha_int = None
    qtd_opcoes = len(opcoes)
    if escolha.isdigit():
        escolha_int = int(escolha)


    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <= qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
                
    if acertou:
        print ("Parabéns você acertou!")
        acerto += 1
    else:
        print("infelizmente você errou!")
        erro += 1
        

if acerto == 3:
    print(f'Você acertou: {acerto}')
elif erro == 3:
    print(f'Você errou: {erro}')
    print("Estude mais!")
else:
    print(f"Você acertou: {acerto}")
    print(f'Você errou: {erro}')
