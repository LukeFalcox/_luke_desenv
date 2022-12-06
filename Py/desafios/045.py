import random
print("""
   [1]Pedra
   [2]Tesoura
   [3]Papel""")
escolha = int(input("Escolha uma opção: "))
comp = random.randint(1,3)
if comp == escolha:
    print('Empate')
elif escolha == 1 and comp == 2 or escolha == 2 and comp == 3 or escolha == 3 and comp == 1:
    print('Vitoria')
elif escolha == 2 and comp == 1 or escolha == 3 and comp == 2 or escolha == 1 and comp == 3:
    print('Derrota')
