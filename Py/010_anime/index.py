c = 1
par = impar = 0
while c == 0:
    print('\033m', c ,'\033m')
    c+= 1
print('Fim')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input("Quer continuar? [S/N]")).upper()
t = 1
while t != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if t % 2 == 0:
            par +=1
        else:
            impar +=1