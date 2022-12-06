lanche = 'Hambuguer' #<- Variaveis Simples
lanche = ('Hambuguer','Suco','Pizza','Sorvete') #<- Variaveis Compostas
print(lanche[2])
print(lanche[0:2])
print(lanche[1:])
print(lanche[:3])
print(lanche[-1])
print(lanche[:-1])
print(lanche[-1:])
print(sorted(lanche))
len(lanche)
for c in lanche:
    print(c)
for comida in lanche:
    print(f"Eu vou comer {comida}")
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}') 
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(2))
pessoa = ('Gustavo',39,'M',99.88)
print(pessoa)