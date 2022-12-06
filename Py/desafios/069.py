p=0
h=0
m=0
while True:
    idade = int(input("Qual a sua idade:"))
    sexo = str(input("Qual seu sexo:"))
    sexo = sexo.capitalize()
    if idade >= 18:
        print('alert')
        p = p+1
        if sexo == 'M':
            print('alert M')
            h =1+h
        elif sexo == 'F' and idade < 20:
            print('alert F')
            m=1+m
    usu = str(input("Voce deseja que o programa pare: "))
    usu = usu.capitalize()
    if usu == 'Sim' or 'S':
        break
    elif usu == 'Nao' or 'N':
        print('------------------------------')
print("Tem {} pessoas adultas".format(p))
print("Tem {} mulheres abaixo de vinte anos".format(m))
print("Tem {} homens".format(h))