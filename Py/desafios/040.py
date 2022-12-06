nota1 = float(input("Qual a sua primeira nota"))
nota2 = float(input("Qual a sua segunda nota"))
media = (nota1 + nota2) / 2
if media < 5.0 :
    print("Reprovado")
    print(media)
elif media < 5.0 and 6.9:
    print("Recuperação")
    print(media)
elif media >= 7.0:
    print("Aprovado")
    print(media)