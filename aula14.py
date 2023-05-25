a = 'A'
b = 'B'
c = 1.1
c2 = 2.0
string = 'a={nome1} b={nome2} c{nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c,)
teste = c2
print(formato, teste)
