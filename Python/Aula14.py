a = 'A'
b = 'B'
c = 1.1

#Tudo no Python um objeto, com isso faz com que e caracterizado métodos para serem feitos dentro das string como "format"
# dentro do parenteses ele vai dá argmentos para o "format"
string = 'a={}, b={}, c={:.2f}'
#nesse caso abaixo seria para duplicar o valor e não depender da ordem do número. Como e o padrão que seria lendo a ordem de a, b e c
#nesse caso o a tem o valor de "0", o b tem valor de "1" e o c tem o valor de "2", 
# por causa que na programação a númeração de módulos ou outras coisas como paramnetros sempre começa no "0"
string2 = 'b={1},b={1}, a={0},a={0},a={0},a={0}, c={2:.2f}'
#'Replacement index 3 out of range for positional args tuple' caso apareça esse erro e que não tem o método para buscar, 
# caso tivesse qualquer outro valor lá dentro iria ser mostrado. Pois vai buscar algo que já acabou e vai mostrar esse erro.
string3 = 'b={nome2}, a={0}, c={nome3:.2f}'
#o parametro a e b, vão continuar funcionando pois não está nomeado, mas o parametro c não vai pois foi nomeado para "nome3" 
formato =string.format(a, b, c)
formato_2 =string2.format(a, b, c)
formato_3 =string3.format(a, nome2=b, nome3=c)# nome2 e um parametro nomeado. Que é um parametro, onde vai está se referindo ao valor do C que e um argumento.
#caso um argumento seja nomeado, os posteriores devem ser nomeados também para que não haja erro. 
# no python se chama parametro nomear, quando damos nome a algo que por sua vez está nomendo as funções que estão sendo chamado, 
#isso também e quando cria as funções. 
#como segue exempo abaixo

print (formato)
print (formato_2)
print (formato_3)