import random 
import time
kont = 0
comp = random.randint(0, 10)
usu = int(input('Fale o numero que o computador pensou:'))
while usu != comp:
    kont+=1
    usu = int(input('Fale denovo que o computador pensou:'))
    time.sleep(1)
print('Voce acertou')
time.sleep(2)
print("Numeros de tentativas {}".format(kont))
