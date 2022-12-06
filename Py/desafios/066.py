n = s = 0
while True:
    n = int(input("Digite um numero (999 faz parar): "))
    if n==999:
        break
    s+=n
print("A soma vale {}".format(s))