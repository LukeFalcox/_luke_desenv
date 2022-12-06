import random
Primeiro = str(input("Primeiro aluno:"))
Segundo = str(input("Segundo aluno:"))
Terceiro = str(input("Terceiro aluno:"))
Quarto = str(input("Quarto aluno:"))
lista = [Primeiro,Segundo,Terceiro,Quarto]
random.shuffle(lista)
print(lista)