n1 = int(input("Primeiro termo:"))
r = int(input("Razao:"))
d = n1 + (10-1) * r
for c in range(n1,d + r,r):
    print("{}".format(c), end='->')