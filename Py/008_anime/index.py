nome = str(input("Qual seu nome: "))
if nome == 'Dante':
    print('\033[0;33mQue nome mais diferente')
elif 'Pedro' or 'Lucas' or 'Amanda' or 'Ana':
    print('SEu nome é bem comum no Brasil')
elif nome in 'Jose Claudio Jeremiaz Creuza':
    print('Seu nome é bem incomum')
else:
    print("Que nome legal")
print("Até mais {}{}".format('\033[7;30m',nome))