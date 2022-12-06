m = int(input('A velocidade do seu carro: '))
if m>=80:
    multa = m-80
    resultado = multa*7
    print('Voce foi multado pague: {}'.format(resultado))
else:
    print('Voce esta na velocidade ideal')