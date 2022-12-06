#Operadores Aritmeticos
# + = Adição
# - = Subtração
# * = Multiplicação
# / = Divisão
# ** = Potencia
# // = Divisao inteira
# % = Resto da divisao

#Todos operadores precisam de um operando como numeros ou letras, e ate coisa como numeros e letras
#E alguns operadores se chamam de operadores binarios que precisam de outros operadores olhe o exemplo a seguir

#5+2==7
#5-2==3
#5*2==10
#5/2==2.5
#5**2==25
#5//2==2
#5%2==1
# a diferença dentre para o outro igua =,== é que o = indica que o valor recebe e o outro == pergunta  por exemplo cinco mais dois é igual a quanto?

#Ordem de precendencia
#1()
#2**
#3*,/,//,%
#4+,-
#exemplo 1
# n5+3*2==11
#Olhe a ordem de precedencia que vem primeiro na tabela o * entao a conta sera começado em 3*2 e depois so somar +5== 11
#exemplo 2
#3*5+4**2==31
#O mesmo assunto a potencia representada por ** vai ser a conta que deve ser iniciada e em seguida a * e voce ira somar os dois fatores
#exemplo 3
#3*(5+4)**2
#Tudo oque tiver dentro dos parenteses vai ter a maior precedencia entao oq tiver dentro dos parenteses vai ser feito primeiro

#nome = input('Qual seu nome')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

from uuid import NAMESPACE_X500


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, o produto é {}, e a divisao é {:.3f}'.format(s, m, d, end=''))
print('a Divisão inteira é {}, o potencia é {}'.format(di, e))
# Esse codigo {:.3f} serve para definir quantas casas decimais de um dizma ou de qualquer numero ser aumentado por exemplo 4/3 = 1.3333333, mas esse codigo vai diminuir para a quantidade do numero que tiver dentro da chave se tiver assim {:.3f} entao o numeros de casa vai ser tres "1.333"
# esse end='' serve para nao quebrar a linha no resultado, e se voce querer quebrar a linha coloca /n depois da chave assim '/n a soma é {}, /n o produto é {}, /n e a divisao é {:.3f}, e se quiser colocar um efeito tipo >>>> para a prxima conta no end='' coloca o que vc quiser'.


