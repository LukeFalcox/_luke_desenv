saque = int(input("Que valor voce quer sacar? R$"))
tot = 0
tut = 0
tit = 0
tet = 0
while True:
    if saque > 49:
        while saque > 49: 
            tot = tot + 1
            saque = saque - 50
    elif saque > 19:
        while saque > 19:
            tit = tit + 1
            saque = saque - 20
    elif saque > 9:
        while saque > 9:
            tet = tet + 1
            saque = saque - 10
    elif saque > 0:
        while saque > 0:
            tut = tut + 1
            saque = saque - 1
    elif saque == 0:
        break
print("Total de {} Cedulas de R$50".format(tot))
print("Total de {} Cedulas de R$20".format(tit))
print("Total de {} Cedulas de R$10".format(tet))
print("Total de {} Cedulas de R$1".format(tut))
    
    