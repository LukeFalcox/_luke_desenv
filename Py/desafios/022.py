nome = input('Qual o seu nome: ')
print("O nome com todas as letras maiuscula {}".format(nome.upper()))
print("O nome com todas as letras minusculas {}".format(nome.lower()))
n1=nome.replace(' ','')
print("A quantidade de letras sem considerar os espaços de é {}".format(len(n1)))
dividido = nome.split()
print(dividido[0])