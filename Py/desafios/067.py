n = int(input("Digite um numero para tabuada: "))
s = 0
while True:
    t = n * s
    print("{} vezes {} = {}".format(n,s,t))
    s=s+1
    if s == 11:
        break
    