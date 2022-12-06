# import random
# a1 = str(input('Primeiro aluno: '))
# a2 = str(input('Segundo aluno: '))
# print('Sorteio: {}'. format(random.choice([a1, a2])))
# import random
# tot = 1
# while True:
#     comp = random.randint(1,2)
#     if comp == 1:
#         print("O computador escolheu Par")
#     elif comp == 2:
#         print("O computador escolheu Impar")
#     op = int(input("Escolha Par ou impar:"))
#     numero = int(input("Digite um numero:"))
#     numero2 = random.randint(0,10)
#     if op == 1 or op == 2:
#         soma = numero + numero2
#         resultado = soma%2
#     if resultado == 0 and op == 'Par' and comp == 2:
#             print("Voce Ganhou")
#             tot = tot+1
#     elif resultado == 0 and op == 'Impar' and comp == 1:
#             print("Voce Perdeu")   
#             break 
#     elif resultado == 1 and op == 'Impar' and comp == 1:
#             print("Voce Ganhou")
#             tot = tot+1
#     elif resultado == 1 and op == 'Par' and comp == 2:
#             print("Voce Perdeu")
#             break
#     elif resultado == 1 or resultado == 0 and op == 'Impar' and comp == 2 or op == 'Par' and comp == 1:
#         print("Erro!!!")
# print("A sua sequencia de vitorias foi {}".format(tot))
import random
tot = 1
while True:
    op = str(input("Escolha Par ou Impar:"))
    op = op.title()
    if op == 'Par':
            print('O computador será Impar')
            comp = 'Impar'
    elif op == 'Impar':
            print('O computador será Par')
            comp = 'Par'
    numero = int(input("Digite um numero:"))
    numero2 = random.randint(0,10)
    if op == 'Par' or op == 'Impar':
        soma = numero + numero2
        resultado = soma%2
        print(resultado)
    if resultado == 0 and op == 'Par' and comp == 'Impar':
            print("Voce Ganhou")
            print("O computador escolheu {}".format(numero2))
            tot = tot+1
    elif resultado == 0 and op == 'Impar' and comp == 'Par':
            print("Voce Perdeu")   
            print("O computador escolheu {}".format(numero2))
            break 
    elif resultado == 1 and op == 'Impar' and comp == 'Par':
            print("Voce Ganhou")
            print("O computador escolheu {}".format(numero2))
            tot = tot+1
    elif resultado == 1 and op == 'Par' and comp == 'Impar':
            print("Voce Perdeu")
            print("O computador escolheu {}".format(numero2))
            break
print("A sua sequencia de vitorias foi {}".format(tot))
            