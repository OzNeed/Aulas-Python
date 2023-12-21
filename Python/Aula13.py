nome = 'Luiz Otávio'
altura = float (1.80)
peso = 95
imc = peso / (altura*altura)

#print(nome,'tem', altura, 'de altura')
#print('pesa',peso, 'e o seu IMC é:', imc)

# o 'f' antes da string seria para habilitar a formatação dentro dela, como segue exemplo abaixo. 
# Para puxar mais de uma casa decimal deve ser feito o seguinte processo ":.""quantas casas decimais você quer"
'f-string' # "F" vem de formatação
linha_de_texto1 = f"{nome} tem {altura:.2f} de altura"
linha_de_texto2 = f"pesa {peso} e o seu IMC é {imc:.2f}"
print(linha_de_texto1)
print(linha_de_texto2)