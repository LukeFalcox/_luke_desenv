gasto = 0
tot = 0 
barato = 0
produto = ''
while True:
    nome = str(input("Qual é o Produto:"))
    preço = int(input("Qual é o valor do seu Produto:"))
    gasto = preço + gasto
    if preço > 1000:
        tot = tot + 1
    else:
        tot = tot + 0
    if barato == 0:
        barato = preço
    elif barato > preço:
        barato = preço
        produto = nome
    resposta = str(input("Voce deseja que o programa Pare?\nS/N:"))
    resposta = resposta.capitalize()
    if resposta == 'S':
        print('-'*30)
        print('Obrigado pela preferencia')
        break
    elif resposta == 'N':
        print('-'*30)
print("O total do gasto é de {}".format(gasto))
print("Tem {} Produtos que custam mais de 1000R$".format(tot))    
print("O {} é o produto mais barato na loja valendo {}R$".format(produto,barato))
        