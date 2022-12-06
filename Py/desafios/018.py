import math
ang = float(input('Digite um angulo'))
seno = math.sin(math.radians(ang))
print('O angulo de {} tem seno de {:.2f}'.format(ang,seno))
cose = math.cos(math.radians(ang))
print('O angulo de {} tem cosseno de {:.2f}'.format(ang,cose))
tang = math.atan(math.radians(ang))
print('O angulo de {} tem cosseno de {:.2f}'.format(ang,tang))