cpf_digitado = '74682489070'
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