N = int(input("Digite um numero inteiro: "))
print("Escolha um desse para converter seu numero \n1 = Binario \n2 = Octal \n3 = Hexadecimal")
E = int(input("Digite o numero"))
if E == 1:    
    print("O seu numero em Binario é {}".format(bin(N)[2:]))
elif E == 2:
 print("O seu numero em Octal é {}".format(oct(N)[2:]))
elif E == 3:
     print("O seu numero em Hexadecimal é {}".format(hex(N)[2:]))
else:
    print('Erro!!!!')