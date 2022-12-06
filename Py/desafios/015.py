aluguel = int(input('Quantos dias alugados?: '))
km = int(input('Quantos km rodados?'))
calc = (aluguel*60) + (km*0,15)
print('O total que voce deve a pagar é de {}'.format(calc))