import random
Primeiro = str(input("Primeiro aluno:"))
Segundo = str(input("Segundo aluno:"))
Terceiro = str(input("Terceiro aluno:"))
Quarto = str(input("Quarto aluno:"))
lista = [Primeiro,Segundo,Terceiro,Quarto]
prof = random.choice(lista)
print(prof)