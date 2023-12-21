#\r=return \n=lene feed, isso faz com que o windows quebra a linha ->CRLF
#\n -> LF
print(12, 34, "oie", sep='-', end='  haha\r\n') #arquivos não nomeados e o espaço quando executa
print(56, 78, "olá", sep='-', end="\n") #sep seria para nomear o arquivo não nomeado e consguir separa ele da forma que deseja.

#sep, para nomear o separador
#end, para quebrar a linha ou colocar o que deseja