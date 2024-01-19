cpf_digitado = '74682489070'
nove_digitos = cpf_digitado[:9]
contador_regressivo = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito = (resultado_digito_1 * 10) % 11

digito = digito if digito <= 9 else 0
print(digito)