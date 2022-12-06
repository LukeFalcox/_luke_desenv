ano = int(input("Digite o ano que voce nasceu: "))
idade = 2022 - ano
if idade < 18:
    print('Voce nao deve se alistar')
elif idade == 18:
    print('Voce deve se alistar')
elif idade > 18:
    print('Ja passou a hora de se alista')
tempo = 18 - idade
print('Falta {} para voce se alistar'.format(tempo))