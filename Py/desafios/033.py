N1 = int(input("Digite o Primeiro numero: "))
N2 = int(input("Digite o  Segundo numero: "))
N3 = int(input("Digite o  Terceiro numero: "))
menor = N1
if N2<N1 and N2<N3:
    menor = N2
if N3<N1 and N3<N2:
    menor = N3
#Verificando o maior
maior = N1
if N2>N1 and N2>N3:
    maior = N2
if N3>N1 and N3>N2:
    maior = N3
print("O Maior valor é {}".format(maior))
print("O Menor valor é {}".format(menor))
    
