Km = int(input('Qual a distancia da sua viagem: '))
if Km<=200:
    preço = Km*0.50
    print('O preeço da passagem é de {}'.format(preço))
else:
    preço = Km*0.45
    print('O preeço da passagem é de {}'.format(preço))
print('FIM DO PROGRAMA')