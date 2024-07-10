"""
Clousure e funções que retornam outras funções
"""
# A saudacao será lembrado, porém o nome não
def criar_suadacao(saudacao):
    def saudar(nome): #vai atrasar um pouco mais o código, mas vai ficar muito mais editavél e legivel
        return f'{saudacao}, {nome}!'
    return saudar



falar_bom_dia = criar_suadacao('Bom dia')
falar_boa_noite = criar_suadacao('boa noite')

for nome in ['Bruno', 'Bruna', 'Celma']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))