'''Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas.No final do programa, mostre:
A media de idade do grupo "Concluido"
Qual é o nome do homem mais velho "Concluido"
Quantas Mulheres tem menos de 20 anos "Concluido"
Programa "CONCLUIDO"
'''
maior = 0
tot = 0
cont_i = 0
cont_nome = ''
for p in range(1,5):
    print("-----{}° Pessoa -----".format(p))
    nome = str(input("Nome:"))
    idade = int(input("Idade:"))
    sexo = str(input("Sexo:"))
    if p == 1:
        cont_i = idade    
        if sexo == 'M':
            maior = idade
            cont_nome = nome
        if sexo == 'F' and idade<=20:
            tot+=1
    elif p == 2:
        cont_i = idade
        if sexo == 'M' and idade>maior:
            maior = idade
            cont_nome = nome
        if sexo == 'F' and idade<=20:
            tot+=1
    elif p == 3:
        cont_i = idade
        if sexo == 'M' and idade>maior:
            maior = idade
            cont_nome = nome
        if sexo == 'F' and idade<=20:
            tot+=1
    elif p == 4:
        cont_i = idade
        if sexo == 'M' and idade>maior:
            maior = idade
            cont_nome = nome
        if sexo == 'F' and idade<=20:
            tot+=1
media = cont_i/4
print("A media da idade é de {}".format(media))
print("O nome do homem {} mais velho {}".format(maior,cont_nome))
print("Mulheres tem menos de 20 anos {}".format(tot))