menu = 4
while menu == 4:
    n1 = int(input("Digite o primeiro valor:"))
    n2 = int(input("Digite o primeiro valor:"))
    menu = int(input("\n(1-somar)\n(2-mutiplicar)\n(3-maior)\n(4-novos numeros)\n(5-sair do progarma)\nEscreva aqui a sua escolha de opção:"))
    if menu == 1:
            resul= n1 + n2 
            print(resul)
    elif menu == 2:
        resul= n1 * n2 
        print(resul)
    elif menu == 3:
        if n1 > n2:
            print("O maior numero é {}".format(n1))
        else:
            print("O maior numero é {}".format(n2))
        
    