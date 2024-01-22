import re
import sys

# cpf_digitado = '746.824.890-70'.replace('.', '').replace('-', '')#Para remover o dígito que deseja, a primeira aspas para informa o que deseja remover, logo em seguida pelo que deseja trocar como na segunda aspas.

entrada = input('CPF [746.824.890-70]: ')

cpf_digitado = re.sub(
    r'[^0-9]',
    '',
    entrada
    )
#o re.sub ele serve para remover e trocar de forma mais simples, como no exemplo acima. Deve ser inserido antes da string o re.sub, logo em seguica o r'' de expressão regular para informa qualquer coisa que não esteja dentro das chaves [^0-9], como isso seria para não remover nenhu número. Ai logo em seguida o que deseja ser alterado e após isso e a string que deseja formatar.

primeiro_e_sequencial = entrada == entrada[0] * len(entrada)

if primeiro_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_digitado[:9]
contador_regressivo = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo
    contador_regressivo -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo
    contador_regressivo -= 1
digito_2 = (resultado_digito_2* 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_digitado == cpf_gerado_pelo_calculo:
    print(f'{cpf_digitado} é valido')
else:
    print('CPF inválido')