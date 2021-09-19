n1 = int(input('Um valor:'))
n2 = int(input('Outro valor: '))
s = n1+n2
n = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {},\n o produto é {} e a divisão é{:.3f} '.format(s,n,d),end=' ')
print('Divisão inteira {} e potência {} '.format(di,e))