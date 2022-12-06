A = int(input("Digite o Reta 1: "))
B = int(input("Digite o  Reta 2: "))
C = int(input("Digite o  Reta 3: "))
if A == B == C:
    print('È um triangulo equilatero')
elif A == B != C or A == C != B or B == C != A:
    print('È um triangulo isoceles')
elif A != B != C:
    print('È um triangulo escaleno')

