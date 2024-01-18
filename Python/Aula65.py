"""
Operação ternária (condicional de uam linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'outro valor'
# print(variavel)

# digito = int(input('Digite um número: ')) # 9 >0
# # novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

print('Valor' if True else 'Outro valor' if True else 'Fim')
print('Valor' if False else 'Outro valor' if True else 'Fim')
print('Valor' if False else 'Outro valor' if False else 'Fim')