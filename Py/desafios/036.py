V = float(input("Qual o valor da casa "))
S = float(input("Qual o seu salario "))
A = int(input("Quantos Anos voce deseja pagar a casa "))
M = A * 12
T = V / M
E = S * 0.3
if E>T:
    print("Voce consegue pagar esta casa")
    print(T)
    print(E)
elif E<T:
    print("Voce nao pode pagar esta casa")
