# while true:
#     if Bloco:
#         passo
#     if espaço:
#         pula
#     if moeda:
#         pega
#     if trofeu:
#         pega
#         break;
n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n==999:
        break
    s+=n
print("A soma vale {}".format(s))