# fatiamento de strings 
# 012345678
# Ola mundo
# -987654321
# Fatiamento [i:f:p] [::]
# obs.: a função len retorna a qtd de caracteres da str

variavel = 'olá mundo'
print(variavel[5:]) #para determinar onde começar digite o índice de onde quer que o python leia
#para determinar onde termina, omita o final (assim ele saberá que precisa ler até o fim) ou coloque um índice a mais, pois o python sempre mostra como índice final o anterior do qual você marcou
#caso omita o inicio ele começará do inicio, caso omita o fim ele irá ler até o fim, caso queira regrar, digite o índice que quer fazer o fatiamento
print(len(variavel))# função len mostra quantos caractéres tem a string que está envolvida na função, sabendo que índice e caracteres são diferentes,
#índice começa do 0 e caracteres do 1.
print(variavel[::-1])#posso usar o :p para inverter a palavra, usando o índice negativo
print(variavel[::2])#posso usar o :p para determinar de quantos em quantos ele ira contar, 1 vai contar todos os carecteres, 2 conta um e pula outro etc...

