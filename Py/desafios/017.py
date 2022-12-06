from math import pow,sqrt
catop = int(input('Digite o comprimento do cateto oposto: '))
catad = int(input('Digite o comprimento do cateto adjacente: '))
hipot = catop**2 + catad**2
result = sqrt(hipot)
print('O valor da hipotenusa é de {}'.format(result))