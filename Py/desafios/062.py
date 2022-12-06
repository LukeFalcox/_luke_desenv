n1 = int(input("Primeiro termo:"))
n2 = ''
r = int(input("Razao:"))
d = n1 + (10-1) * r
while n2 != 0:
    while n1 <= d:
        print("{}".format(n1), end='->')
        n1+=r
    n2 = int(input("\nMais quantos termos :"))
    d = n1 + n2 * r
        

    
    