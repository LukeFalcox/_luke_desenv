frase = str(input("Digite um palindromo"))
frase = frase.replace(' ','')
for c in range(0,1):
    reverso =''.join(reversed(frase))
if frase == reverso:
    print("A frase é um palindromo")
else:
    print("A frase nao é um palindromo")