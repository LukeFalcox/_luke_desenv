preço = float(input("Qual o preço do seu produto: "))
print("""
 [1] À Vista no dinheiro/cheque  (10% de desconto)
 [2] À Vista no cartão (5% de desconto)
 [2] 2x no cartao (preço normal)
 [2] 3x ou mais (20% de juros)
      """)
CDP = print(input("Qual é sua forma de pagamento: "))
if CDP == 1:
    desconto = preço * 0.10
    print("O seu produto com desconto fica {}".format(desconto))
elif CDP == 2:
    desconto = preço * 0.05
    print("O seu produto com desconto fica {}".format(desconto))
elif CDP == 3:
    print("O seu produto esta com preço normal {}".format(preço))
elif CDP == 4:
    juros = preço / 0.20
    print("O seu produto com juros fica {}".format(juros))