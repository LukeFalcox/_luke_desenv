import random
comp = random.randint(0, 5)
usu = int(input('Fale o numero que o computador pensou:'))
if usu == comp:
    print('Parabens')
else:
    print('KKK Loser')
    print('O computador escolheu o numero {}'.format(comp))