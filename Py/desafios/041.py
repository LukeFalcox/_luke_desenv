ano = int(input("Digite o ano que voce nasceu: "))
idade = 2022 - ano
if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Senior")
elif idade > 20:
    print("Master")