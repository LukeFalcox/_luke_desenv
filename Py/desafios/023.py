Numero = int(input('Digite um numero de 0 ha 9999: '))
u = Numero // 1 % 10
d = Numero // 10 % 10
c = Numero // 100 % 100
m = Numero // 1000 % 1000
print('Analizando o numero {}'.format(Numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
