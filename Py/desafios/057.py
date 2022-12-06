"""
Faça um Programa que:
Leia O sexo de uma pessoa
Mas só aceite valores 'M' 'F'.
Caso esteja errado peça a digiteação novamente ate ter um valor correto
"""

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Daddos invalidos. Porfavor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))