n = 0
t = 1
a = 0
while n != 999:
    print('999 é a condição para parar')
    n = int(input("Digite qualquer numero: "))
    t = t + t
    a = a + n
a = a - 999
print("A soma entre todos o numeros é {}{}".format('\033[32m',a))