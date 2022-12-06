from re import A


A = int(input("Digite o Reta 1: "))
B = int(input("Digite o  Reta 2: "))
C = int(input("Digite o  Reta 3: "))
if A < B + C and B < A + C and C < A + B:
    print("Pode ser feito um triangulo")
else:
    print('Nao pode ser feito o triangulo')
