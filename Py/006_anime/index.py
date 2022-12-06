#Condições
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--Fim--')
'''-----------------------------'''
nome = str(input('Qual é o seu nome? '))
if nome == 'Dante':
    print('Que nome lindo voce tem! ')
else:
    print('Seu nome é tao normal')
print('Bom dia {}'.format(nome))
'''-----------------------------'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua media foi {:.1f}'.format(m))
if m>=6.0:
    print('Aprovado')
else:
    print('Reprovado')