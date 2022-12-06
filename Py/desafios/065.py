n1 = 0
a = 0
t = 1
p ='S'
while p == 'S':
    n = int(input("Digite qualquer numero: "))
    a = a + n
    t = t + t
    p = str(input("quer digitar mais valores "))
media = a / t
print(media)