tot = 0
for c in range(0,7):
    ano = int(input("\nQual o seu ano de nascimento: "))
    if 2022-ano >= 18:
        print("\033[33mVoce é maior de idade\033[32m", end='')
        tot += 1
    else:
        print("\033[33mVoce é não maior de idade", end='')
    print('\n{}'.format(c), end='')
N = 7 - tot
print("\n{} pessoas atigiram a maioridade e {} nao atigiram".format(tot,N))
